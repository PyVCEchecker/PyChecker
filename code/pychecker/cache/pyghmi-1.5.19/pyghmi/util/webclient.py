# Copyright 2015-2019 Lenovo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This provides ability to do HTTPS in a manner like ssh host keys for the
# sake of typical internal management devices.  Compatibility back to python
# 2.6 as is found in commonly used enterprise linux distributions.

import base64
import copy
import gzip
import io
import json
import socket
import ssl
import threading

import six

import pyghmi.exceptions as pygexc

try:
    import Cookie
    import httplib
except ImportError:
    import http.client as httplib
    import http.cookies as Cookie


# Used as the separator for form data
BND = b'TbqbLUSn0QFjx9gxiQLtgBK4Zu6ehLqtLs4JOBS50EgxXJ2yoRMhTrmRXxO1lkoAQdZx16'

# We will frequently be dealing with the same data across many instances,
# consolidate forms to single memory location to get benefits..
uploadforms = {}


class FileUploader(threading.Thread):

    def __init__(self, webclient, url, filename, data=None, formname=None,
                 otherfields=()):
        self.wc = webclient
        self.url = url
        self.filename = filename
        self.data = data
        self.otherfields = otherfields
        self.formname = formname
        self.rsp = ''
        self.rspstatus = 500
        super(FileUploader, self).__init__()

    def run(self):
        try:
            self.rsp = self.wc.upload(
                self.url, self.filename, self.data, self.formname,
                otherfields=self.otherfields)
        except Exception:
            self.rspstatus = self.wc.rspstatus
            raise


class FileDownloader(threading.Thread):

    def __init__(self, webclient, url, savefile):
        self.wc = webclient
        self.url = url
        self.savefile = savefile
        self.exc = None
        super(FileDownloader, self).__init__()

    def run(self):
        try:
            self.wc.download(self.url, self.savefile)
        except Exception as e:
            self.exc = e


def get_upload_form(filename, data, formname, otherfields):
    if not formname:
        formname = filename
    try:
        return uploadforms[filename]
    except KeyError:
        try:
            data = data.read()
        except AttributeError:
            pass
        form = (b'--' + BND
                + '\r\nContent-Disposition: form-data; '
                  'name="{0}"; filename="{1}"\r\n'.format(
                      formname, filename).encode('utf-8'))
        form += b'Content-Type: application/octet-stream\r\n\r\n' + data
        for ofield in otherfields:
            form += (b'\r\n--' + BND
                     + '\r\nContent-Disposition: form-data; '
                       'name="{0}"\r\n\r\n{1}'.format(
                           ofield, otherfields[ofield]).encode('utf-8'))
        form += b'\r\n--' + BND + b'--\r\n'
        uploadforms[filename] = form
        return form


class SecureHTTPConnection(httplib.HTTPConnection, object):
    default_port = httplib.HTTPS_PORT

    def __init__(self, host, port=None, key_file=None, cert_file=None,
                 ca_certs=None, strict=None, verifycallback=None, clone=None,
                 **kwargs):
        if 'timeout' not in kwargs:
            kwargs['timeout'] = 60
        self.mytimeout = kwargs['timeout']
        self._currdl = None
        self.lastjsonerror = None
        self.broken = False
        self.thehost = host
        self.theport = port
        try:
            httplib.HTTPConnection.__init__(self, host, port, strict=strict,
                                            **kwargs)
        except TypeError:
            httplib.HTTPConnection.__init__(self, host, port, **kwargs)
        if clone:
            self._certverify = clone._certverify
            self.cookies = clone.cookies
            self.stdheaders = copy.deepcopy(clone.stdheaders)
        else:
            self._certverify = verifycallback
            self.cookies = {}
            self.stdheaders = {}
        if self._certverify:
            self.cert_reqs = ssl.CERT_NONE  # use custom validation
        else:
            self.cert_reqs = ssl.CERT_REQUIRED  # use standard validation
        if '[' not in host and '%' in host and 'Host'not in self.stdheaders:
            self.stdheaders['Host'] = '[' + host[:host.find('%')] + ']'

    def dupe(self):
        return SecureHTTPConnection(self.thehost, self.theport, clone=self,
                                    timeout=self.mytimeout)

    def set_header(self, key, value):
        self.stdheaders[key] = value

    def set_basic_credentials(self, username, password):
        if isinstance(username, bytes) and not isinstance(username, str):
            username = username.decode('utf-8')
        if isinstance(password, bytes) and not isinstance(password, str):
            password = password.decode('utf-8')
        authinfo = ':'.join((username, password))
        if not isinstance(authinfo, bytes):
            authinfo = authinfo.encode('utf-8')
        authinfo = base64.b64encode(authinfo)
        if not isinstance(authinfo, str):
            authinfo = authinfo.decode('utf-8')
        self.stdheaders['Authorization'] = 'Basic {0}'.format(authinfo)

    def connect(self):
        addrinfo = socket.getaddrinfo(self.host, self.port)[0]
        # workaround problems of too large mtu, moderately frequent occurance
        # in this space
        plainsock = socket.socket(addrinfo[0])
        plainsock.settimeout(self.mytimeout)
        try:
            plainsock.setsockopt(socket.IPPROTO_TCP, socket.TCP_MAXSEG, 1456)
        except socket.error:
            pass
        plainsock.connect(addrinfo[4])
        if self._certverify:
            self.sock = ssl.wrap_socket(plainsock, cert_reqs=self.cert_reqs)
            bincert = self.sock.getpeercert(binary_form=True)
            if not self._certverify(bincert):
                raise pygexc.UnrecognizedCertificate('Unknown certificate',
                                                     bincert)
        else:
            ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            ctx.load_default_certs()
            ctx.verify_mode = ssl.CERT_REQUIRED
            ctx.check_hostname = True
            self.sock = ctx.wrap_socket(plainsock,
                                        server_hostname=self.thehost)

    def getresponse(self):
        try:
            rsp = super(SecureHTTPConnection, self).getresponse()
            try:
                hdrs = [x.split(':', 1) for x in rsp.msg.headers]
            except AttributeError:
                hdrs = rsp.msg.items()
            for hdr in hdrs:
                if hdr[0] == 'Set-Cookie':
                    c = Cookie.BaseCookie(hdr[1])
                    for k in c:
                        self.cookies[k] = c[k].value
        except httplib.BadStatusLine:
            self.broken = True
            raise
        return rsp

    def grab_json_response(self, url, data=None, referer=None, headers=None):
        self.lastjsonerror = None
        body, status = self.grab_json_response_with_status(
            url, data, referer, headers)
        if status == 200:
            return body
        self.lastjsonerror = body
        return {}

    def grab_json_response_with_status(self, url, data=None, referer=None,
                                       headers=None, method=None):
        webclient = self.dupe()
        if isinstance(data, dict):
            data = json.dumps(data)
        if data:
            if not method:
                method = 'POST'
            webclient.request(method, url, data, referer=referer,
                              headers=headers)
        else:
            if not method:
                method = 'GET'
            webclient.request(method, url, referer=referer, headers=headers)
        try:
            rsp = webclient.getresponse()
        except httplib.BadStatusLine:
            return 'Target Unavailable', 500
        except ssl.SSLError as e:
            if 'timed out' in str(e):
                return 'Target Unavailable', 500
            raise
        body = rsp.read()
        if rsp.getheader('Content-Encoding', None) == 'gzip':
            body = gzip.GzipFile(fileobj=io.BytesIO(body)).read()
        if rsp.status >= 200 and rsp.status < 300:
            if body and not isinstance(body, str):
                body = body.decode('utf8')
            return json.loads(body) if body else {}, rsp.status
        return body, rsp.status

    def download(self, url, file):
        """Download a file to filename or file object

        """
        if isinstance(file, six.string_types):
            file = open(file, 'wb')
        webclient = self.dupe()
        dlheaders = self.stdheaders.copy()
        if 'Accept-Encoding' in dlheaders:
            del dlheaders['Accept-Encoding']
        webclient.request('GET', url, headers=dlheaders)
        rsp = webclient.getresponse()
        self._currdl = rsp
        self._dlfile = file
        chunk = rsp.read(16384)
        while chunk:
            file.write(chunk)
            chunk = rsp.read(16384)
        self._currdl = None
        file.close()

    def get_download_progress(self):
        if not self._currdl:
            return None
        return float(self._dlfile.tell()) / float(
            self._currdl.getheader('content-length'))

    def upload(self, url, filename, data=None, formname=None,
               otherfields=()):
        """Upload a file to the url

        :param url:
        :param filename: The name of the file
        :param data: A file object or data to use rather than reading from
                     the file.
        :return:
        """
        if data is None:
            data = open(filename, 'rb')
        self._upbuffer = io.BytesIO(get_upload_form(
            filename, data, formname, otherfields))
        ulheaders = self.stdheaders.copy()
        ulheaders['Content-Type'] = b'multipart/form-data; boundary=' + BND
        ulheaders['Content-Length'] = len(uploadforms[filename])
        self.ulsize = len(uploadforms[filename])
        webclient = self.dupe()
        webclient.request('POST', url, self._upbuffer, ulheaders)
        rsp = webclient.getresponse()
        # peer updates in progress should already have pointers,
        # subsequent transactions will cause memory to needlessly double,
        # but easiest way to keep memory relatively low
        try:
            del uploadforms[filename]
        except KeyError:  # something could have already deleted it
            pass
        self.rspstatus = rsp.status
        if rsp.status != 200:
            raise Exception('Unexpected response in file upload: %s'
                            % rsp.read())
        body = rsp.read()
        if rsp.getheader('Content-Encoding', None) == 'gzip':
            body = gzip.GzipFile(fileobj=io.BytesIO(body)).read()
        return body

    def get_upload_progress(self):
        return float(self._upbuffer.tell()) / float(self.ulsize)

    def request(self, method, url, body=None, headers=None, referer=None):
        if headers is None:
            headers = self.stdheaders.copy()
        else:
            headers = headers.copy()
        if method == 'GET' and 'Content-Type' in headers:
            del headers['Content-Type']
        if method == 'POST' and body and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
        if body and 'Content-Length' not in headers:
            headers['Content-Length'] = len(body)
        if self.cookies:
            cookies = []
            for ckey in self.cookies:
                cookies.append('{0}={1}'.format(ckey, self.cookies[ckey]))
            cookies_header = '; '.join(cookies)
            if headers.get('Cookie', None) is None:
                headers['Cookie'] = cookies_header
            else:
                headers['Cookie'] += '; ' + '; '.join(cookies)
        if referer:
            headers['Referer'] = referer
        try:
            return super(SecureHTTPConnection, self).request(method, url, body,
                                                             headers)
        except httplib.CannotSendRequest:
            self.broken = True
            raise
