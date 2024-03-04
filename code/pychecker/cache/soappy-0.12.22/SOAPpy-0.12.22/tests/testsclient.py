#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'
#!/usr/bin/env python
# coding:utf-8

from SOAPpy import SOAPProxy
server = SOAPProxy("http://localhost:8080/")
print server.echo("Hello world")

# vim:set et sts=4 ts=4 tw=80:
