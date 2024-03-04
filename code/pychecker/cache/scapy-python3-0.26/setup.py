#! /usr/bin/env python3

"""
Distutils setup file for Scapy.
"""


from distutils.core import setup


setup(
    name = 'scapy-python3',
    version = '0.26',
    packages=['scapy'],

    # Metadata
    maintainer = 'Eriks Dobelis',
    maintainer_email = 'phaethon@users.noreply.github.com',
    description = 'Packet crafting/sending/sniffing, PCAP processing tool, based on scapy with python3 compatibility',
    license = 'GPLv2',
    url = 'https://github.com/phaethon/scapy',
    keywords = 'network security monitoring packet pcap analytics visualization',
    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Environment :: Console',
      'Operating System :: POSIX',
      'Operating System :: Microsoft :: Windows',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3 :: Only',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
    ]
)
