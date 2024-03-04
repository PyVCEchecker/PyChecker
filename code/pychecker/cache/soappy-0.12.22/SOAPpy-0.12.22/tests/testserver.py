#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'
#!/usr/bin/env python
# encoding:utf-8
from SOAPpy import SOAPServer
def echo(s):
        return s # repeats a string twice
server = SOAPServer(("0.0.0.0", 8080))
server.registerFunction(echo)
server.serve_forever()

# vim:set et sts=4 ts=4 tw=80:
