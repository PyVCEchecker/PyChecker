msg = """
        PIP package scapy-python3 used to provide scapy3k, which was a fork from scapy implementing python3 compatibility since 2016. This package was included in some of the Linux distros under name of python3-scapy. Starting from scapy version 2.4 (released in March, 2018) mainstream scapy supports python3. To reduce any confusion scapy3k was renamed to kamene. \nYou should use either pip package kamene for scapy3k (see http://github.com/phaethon/kamene for differences in use) or mainstream scapy (pip package scapy, http://github.com/secdev/scapy).  
"""
print(msg)
raise Exception(msg)

