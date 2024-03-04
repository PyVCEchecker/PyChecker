# Copyright (c) 2020 Yubico AB
# All rights reserved.
#
#   Redistribution and use in source and binary forms, with or
#   without modification, are permitted provided that the following
#   conditions are met:
#
#    1. Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#    2. Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""
Connects to the first FIDO device found which supports the CredBlob extension,
creates a new credential for it with the extension enabled, and stores some data.
"""
from __future__ import print_function, absolute_import, unicode_literals

from fido2.hid import CtapHidDevice
from fido2.client import Fido2Client
from fido2.server import Fido2Server
from fido2.extensions import MinPinLengthExtension
from getpass import getpass
import sys

try:
    from fido2.pcsc import CtapPcscDevice
except ImportError:
    CtapPcscDevice = None


def enumerate_devices():
    for dev in CtapHidDevice.list_devices():
        yield dev
    if CtapPcscDevice:
        for dev in CtapPcscDevice.list_devices():
            yield dev


# Locate a device
for dev in enumerate_devices():
    client = Fido2Client(dev, "https://example.com")
    if MinPinLengthExtension.NAME in client.info.extensions:
        break
else:
    print("No Authenticator with the MinPinLength extension found!")
    sys.exit(1)

use_nfc = CtapPcscDevice and isinstance(dev, CtapPcscDevice)

# Prepare parameters for makeCredential
server = Fido2Server({"id": "example.com", "name": "Example RP"})
user = {"id": b"user_id", "name": "A. User"}
create_options, state = server.register_begin(user)

# Add MinPinLength extension, attach data
min_pin = MinPinLengthExtension()
create_options["publicKey"]["extensions"] = min_pin.create_dict()

# Prompt for PIN if needed
pin = None
if client.info.options.get("clientPin"):
    pin = getpass("Please enter PIN:")
else:
    print("no pin")

# Create a credential
if not use_nfc:
    print("\nTouch your authenticator device now...\n")

attestation_object, client_data = client.make_credential(
    create_options["publicKey"], pin=pin
)

# Complete registration
auth_data = server.register_complete(state, client_data, attestation_object)
min_pin_length = min_pin.results_for(auth_data)
print("Credential registered, min PIN length: ", min_pin_length)
