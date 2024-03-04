__author__ = 'luckydonald'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
def test():
	import AutosaveDict
	import doctest
	returned = doctest.testmod(AutosaveDict)
	return returned.failed

if __name__ == '__main__':
	test()
	from AutosaveDict import AutosaveDict
	import os
	array = {
		'foo': 'bar',
		'numbers': [1, 2, 3],
		'hurr': 'durr',
		'boolean': True,
		'dev-null': 0
	}
	# test = AutosaveDictObject("test.json", array)
	sys.exit()

