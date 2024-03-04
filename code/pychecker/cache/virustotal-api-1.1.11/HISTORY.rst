.. :changelog:

Release History
---------------

1.1.11 (2019-09-22)
-------------------

**Allow for hash list input in get_file_report**

- https://github.com/blacktop/virustotal-api/pull/28 (credit: @CDuPlooy)

1.1.10 (2018-03-12)
-------------------

**Intel API Fix**

- https://github.com/blacktop/virustotal-api/pull/23 (credit: @leadZERO)

1.1.9 (2018-01-03 aka the day the CPUs fell)
--------------------------------------------

**Intel API Fix**

- https://github.com/blacktop/virustotal-api/pull/22 (credit: @leadZERO)

1.1.7 (2017-05-28)
------------------

**Intel API Fix**

- https://github.com/blacktop/virustotal-api/pull/18 (credit: @doug-the-guy)

1.1.6 (2017-05-14)
------------------

**Py3 Fix**

- Change `e.message` to `str(message)` (credit: [@DeanF](https://github.com/blacktop/virustotal-api/pull/19))

1.1.5 (2017-04-13)
------------------

**API Changes**

- Added Intelligence notifications feed and ability to programmatically delete notifications from the feed. (credit: @keithjjones)

1.1.4 (2017-03-11)
------------------

**Fixed timeout functionality, removed unnecessary methods**

- Fixed the timeout parameter in the PublicApi and removes unnecessary code in the PrivateApi (credit: @mrredamber aka LEGEND)

1.1.3 (2017-02-03)
------------------

**Request Timeout Functionality**

- Adds a timeout parameter to methods that make requests to the VirusTotal API (credit: @mrredamber aka LEGEND)

1.1.2 (2016-04-13)
------------------

**API Changes**

- Re-adding the ability to use files from memory as well as from disk. (credit: @tweemeterjop)

1.1.1 (2016-03-13)
------------------

**API Changes**

- Adding file/url feed private API endpoint.

1.0.9 (2016-01-01)
------------------

**Privacyfixes**

- Fix scan_file (upload to VT), do not leak full path. (credit: @Rafiot)

1.0.8 (2014-12-26)
------------------

**Bugfixes**

- Fixed get_url_report method for the Private API (credit: @John-Lin)

1.0.7 (2014-10-17)
------------------

**Bugfixes**

- Fixed get_network_traffic method to return the pcap data (credit: adrianherrera)

1.0.6 (2014-09-22)
------------------

**Bugfixes**

- Fixed a small typo in the private API's scan_file method (credit: adrianherrera)

1.0.5 (2014-05-18)
------------------

**Bugfixes**

- Fixing README.rst for better PYPI presentation.

1.0.2 (2014-05-18)
------------------

**API Changes**

- Changing folder structure so when people import it it is not dumb :(

1.0.1 (2014-04-14)
------------------

**Bugfixes**

- Trying to fix setup.py for deploying to PYPI.
