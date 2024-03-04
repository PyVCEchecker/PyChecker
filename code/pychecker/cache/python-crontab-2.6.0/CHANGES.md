# Release notes
This is a generated CHANGES file, based on the Git history.



## Version 3.5.7 (2019-07-11) - Updated RADME and special time setting fixes.
 - Attempt a fix of issue #27 (no test suite test)
 - Merge branch 'master' into 'master'
 - update README.rst file
 - Fix #48, specials can't be changed to another time.
 - Bump version for pypi update
 - Fix #41 dead link to github
 - Ignore mypy_cache
 - Fix #39 - Tab next to username will parse correctly
 - Merge remote-tracking branch 'flotus/patch-1'
 - Improve explaination about using the write function
 - fixed environment

## Version 2.3.5 (2018-09-03) - Bump version only for pypi
 - Bump version to fix pypi issues

## Version 2.3.4 (2018-09-03) - Fix some issues
 - Fix some pylint issues and adjust CronItem API
 - Update readme to point to GitLab
 - Fix #35: Test for specific time as reported.

## Version 2.3.3 (2018-05-25) - Fix remove command when using generators and bad types
 - Protect remove command from bad type use and allow generators to use it
 - Name of repr should be CronItem not CronJob

## Version 2.3.2 (2018-05-25) - Fix logging issues
 - Remove impropper log configuration from module to fix #32

## Version 2.3.1 (2018-05-09) - Add line setter attribute handler
 - Provide a way to set lines directly

## Version 2.3.0 (2018-05-09) - Version 2.3.0
 - Add logging tests, bump version, fix pylint issues and depricate py2.6
 - Fix #22 with new test and range
 - Fix #16 by detecting mips uses
 - Add logo and title back in.

## Version 2.2.8 (light)
 - New version, rst readme and some bug fixes
 - Fix remaining ReST issues.
 - We're moving back to restructured text for the readme
 - Add description for environment variables
 - Merge commit '64461023c56916b2186086b4880ebd9c548dd40d'
 - Add explaination to parsing lines
 - Merge commit '637f85d1bf5be35ccfca8a8d8b6cc2513c5202c5'
 - Nope
 - Merge commit 'c7e1628dd209d30a7eb1a87b5cbf03a35edd35af'
 - Unpick the merge and use a global variable for zero padding.
 - Merge commit 'cf097be'
 - Fix #15 with a slightly modified rex

## Version 2.2.7 (2017-11-18) - ansible compatibility
 - Commit changes for 2.2.7 with ansible compatibility
 - Output environment variables as they were input
 - Do not try to parse comments
 - Do not try to attach comments to jobs
 - Allow zero-padding of non-dow items
 - Remove old changelog, use git log

## Version 2.2.6 (2017-11-02) - v2.2.6
 - Fix issues with allowing lines that will cause errors to be rewritten back
 - Fix unlink command
 - Add tests from issues #11

## Version 2.2.5 (2017-10-20) - quotes on empty variables
 - Fix #11 by always using quotes on empty variables

## Version 2.2.4 (2017-08-03) - env controls and schedule logic
 - Bump version
 - Add test for Rudolf's env patch
 - Actually pass crontab env variables to jobs
 - Immediately run pending cronjobs, don't defer them for 2 minutes

## Version 2.2.3 (2017-06-13) - sibling management
 - Bump version
 - Fix #7 by managing siblings better
 - Small improvements to the readme

## Version 2.2.2 (2017-05-04) - regex and spacing
 - Bump version number
 - Fix #6 with the addition of regular expression support in finding commands
 - Fix #5 with better space and quote management

## Version 2.2.1 (2017-04-28) - env fixes
 - Bump version to 2.2.1
 - Fix #4 using a slighly modified moubctez patch
 - Add test for python3 mutations bug
 - Fix #3 which thought an empty env meant no link to previous env

## Version 2.2.0 (2017-04-22) - environment variables
 - Bump to new version for new feature
 - Remove env var test since it's not the right place and has been superseeded.
 - Use system wide coverage modules instead (not sure about this)
 - Update README with new information for env variable access
 - Add new environment handling to fix issue #1

## Version 2.1.2 (2017-04-20) - -m
 - Up a version to push new github links to pypi
 - Improve markdown for github (will break pypi)
 - Move to github in readme
 - Warn when a cron range is backwards
 - Improve support for older python versions (2.6) with ordereddict use.
 - Fix iteration issue during removal of items. fixed bug #1628844
 - Change timeout to -1, which means infinate no timeout for scheduler
 - Improve readme to help with bug#1638533
 - Small fixes to tests

## Version 2.1.1 (2016-07-07) - unicode support
 - Bump version to 2.1.1.
 - Create test for and fix unicode issues with code from ~hung-allan fixes lp:1599372
 - Add backwards range test
 - Add descriptor as optional setup.py extra

## Version 2.1.0 (2016-06-11) - cron-descriptor support
 - Add cron-descriptor support and fix wishlist bug
 - Improve cronslice code and tests

## Version 2.0.2 (2016-06-02) - sunday write loops
 - Fix sunday issues where cron ranges use ranges incorrectly.
 - try a few other asserts to see if it'll fail
 - Add a new test for bug 1172712 to make sure it's saving.
 - Add comment for new release variable
 - bdist_rpm support
 - Commit patch from Costas for new line variables bug lp:1542272
 - Fix bug lp:1539178 and make iterators work a bit better
 - Improve readme to explain write command at the start.

## Version 2.0.1 (2016-01-04) - schedular
 - Version bump
 - Cover shell
 - Protect against an API misuse (from old documentation)
 - Allow python3 to work with tests, fix year issue (damn you leap year)
 - Add basic scheduler functionality, improve logging and shell support
 - Improve cronlog testings coverage

## Version 2.0.0 (2015-12-30) - system and test
 - Tests for python2 and python3 finally agree and don't warn.
 - Fix issues with python3 testing and python3 errors
 - Updated append so they all use append.
 - Improve code coverage and small refacotring of pipe
 - Updated readme for new crontabs module
 - Improve pylint a little bit in crontab module.
 - Add new crontabs module which allows listing and crontab discovery on a filesystem
 - Refactor spool directory in tests
 - Add CronTab object repr for system and user crontabs
 - Seperate out appending git items
 - Ignore swap files
 - Fix env variable name in test
 - Update readme to git
 - Add git ignore doing conversion
 - Update readme and change env api name
 - Tentative support for crontab variables
 - Make remove_all less agressive by making kwargs smarter
 - Improve user selection and stop specifying user if we are already that user.
 - Fix regression where comment data is duplicated. Test for it.
 - Support vixie/systemv crontab comments which proceed tabs
 - Add ability to understand date and datetime objects when setting cron slices
 - Small refectoring of the write_to_user to allow write to handle it anyway.
 - Make sure writing with no user/filename causes an error
 - Add test for new frequency

## Version 1.9.5 (2015-12-21) - testing too
 - Bump version
 - Add an explict frequency per hour
 - Remove weird monkey
 - Test the utf8 support better
 - Improve readme for new validation feature
 - Add slices validator to help when it's needed. Fix validation of special @based values which were very forgiving and could have led to once a day crons being saved as once a minute.

## Version 1.9.4 (2015-07-30) - Relicense from GPLv3 to LGPLv3
 - Slight improvement to testing of every api use
 - Make the multiple field setting clearer and add a test
 - Allow croniter import test to work in python3
 - Check for UTF-8 system language before doing utf-8 checks
 - Move project to LGPLv3 from GPLv3 to improve use of this module as a library

## Version 1.9.3 (2015-03-23) - Tests, coverage and fixes
 - Add test for user replication
 - Merge in Alan Wong's fix for the 6 part comment issue.
 - Handle system cron edge case when parsing 6-part comments
 - Add coverage testing script (not included in installer)
 - Fix cronlog line error discovered recently
 - Upgrade test coverage, runner and compatability.
 - Add comment headers
 - Fix python 3 compat issue.

## Version 1.9.2 (2015-01-19) - write_to_user fix
 - Fix write_to_user method and improve test case. Fix #1412316

## Version 1.9.1 (2015-01-05) - username requirement
 - Fix username requirement for certain platforms

## Version 1.9.0 (2015-01-02) - vixie cron
 - Add vixie cron system crontab compatability mode

## Version 1.8.2 (2014-12-07) - UTF testing bugs
 - Fix utf filename bug when tests run in pip
 - Commit Jordan Metzmeier's testing flag patch
 - Add fixes from debian distribution. utf-8 file opening and some test tweaks

## Version 1.8.1 (2014-06-18) - Sundays, utf8 and zero sequences
 - Version bump
 - Add check for divide by zero on sequences
 - Fix sunday support and add some more testing for ranges
 - Merge in patch from Jakub Bug #1328951 and add test and more robustness for utf-8 handling.

## Version 1.8.0 (2014-05-22) - Set comment, tuples and utf8
 - Updated readme and add set_comment function.
 - Improve UTF8 support with a new test suite and py2 and py3 uupdates
 - Check the tuples for empty attributes

## Version 1.7.3 (2014-05-05) - Warnings, pipe method and fixes
 - Revise user command to use a more generic pipe method
 - Flake8 fixes
 - Add warning about TypeError when using the wrong package.

## Version 1.7.2 (2014-03-04) - User tab testing and fixes
 - Add test for bug #1287412 and fix the error. bump version to 1.7.2

## Version 1.7.1 (2014-02-06) - Windows critical error
 - Fix windows critical error. Bug #1276040
 - Add write_to_user to readme
 - Bump python version support
 - Fix find by time and allow removal all by time
 - Add the final comparison feature
 - Further completion of the refactoring process
 - Add pylintrc and ignore debian
 - Put two frequency methods back which broke the documented api
 - Seperate out CronSlices from a simple list into it's own class, REFACTOR

## Version 1.7.0 (2014-01-04) - Parsed cron, frequency checking, saving as a user
 - Improve writing capability with write_to_user(user=X) function
 - Add missing specials test data
 - Fix log test for 2014 because it's not year sensitive
 - Merge in the very kind patch from Kevin Waddle
 - Fix no user cron exists error from rev 75 for bug #1258926
 - Fix issue with non-iterable elements
 - Add a check to the specials test to make sure it can be iterated over
 - Apply patch from Harun and add test to the frequency suite
 - Fix no user cron exists error
 - Add is_match functions and find by match functions.
 - Update readme file for frequency features
 - Implement frequency feature and set 0.6.0 version
 - Fix missing day reference
 - New username detection added
 - Attempt to clean up according to pylint
 - Add test of frequency feature for future.
 - Some interesting cleanups
 - Add no fork request and cleaner header comment
 - Remove command complexity and test the commands and comments generators
 - Make comment setting/getting more sane and intergrate jonames() feature from ansible's python-crontab copy.
 - Add len (not sure about it though)
 - Fix some puthon3 issues and introduce a length for a crontab
 - Allow setall to set a parsed cron string

## Version 1.6.0 (2013-11-24) - frequency methods, username,pylint
 - Complete adding new features, a setall() method, a parse() method, and a flexible remove_all() method. With tests.

## Version 1.5.2 (2013-11-01) - Test count
 - Test segments with a count rather than a find
 - Add specials tab to test compatability
 - 23 hours not 24

## Version 1.5.1 (2013-10-12) - Min and max and fixes
 - Improve min and max checking and add extra value to set them. Better testing and more fixes.
 - Updated docs for compatability mode
 - Improve compatability for SystemV crontabs
 - Move cronlog dep to allow setup to function

## Version 1.5.0 (2013-10-12) - Docs and API upgrades
 - Improve docs and impliment 'also' clause, bump version to 1.5
 - Updated branding into the archive, but not the package, updated README with branding image.
 - Updated readme for pypi documentation web formatin

## Version 1.4.4 (2013-10-11) - Every method
 - Add every method to job to improve convience

## Version 1.4.3 (2013-07-28) - Nudges
 - Improve testing for python3 and patch in some nudges

## Version 1.4.2 (2013-05-28) - Line feeds and stderr
 - Bump version for next release when ready
 - Make sure out ending line-feed doesn't proliferate.
 - Pipe stderr in

## Version 1.4.1 (2013-04-10) - Fix dateutils and deps
 - Fix dateutils
 - Fix deps for setup utils
 - Move testing data into a directory
 - Updated tests for opening crontab

## Version 1.4.0 (2013-04-06) - Log reading and croniter functions
 - Complete log testing and fixes
 - First progress towards log parsing
 - Attempt to help windows users
 - Add optional croniter support, clean up some items, write test and update readme
 - Allow for empty lines
 - Protect comments that break detection
 - Minor corrections
 - Bug fixed by George Cox, thanks for the patch

## Version 1.3.2 (2013-03-13) - is_enabled and fixes
 - Spelling mistake
 - Enable and disable documentation
 - Add is_enabled

## Version 1.3.1 (2013-03-13) - Disable jobs
 - Disable and enable crontab jobs
 - Update readme file
 - Update readme file

## Version 1.3.0 (2013-03-12) - Comment finding
 - Ver 1.3 add comment finding and test rendering of comments.
 - Fix
 - Post readme to pypi
 - Update readme
 - Add loading of tabs from files
 - Ignore cache
 - Reinstate python3 comptability

## Version 1.2.0 (2012-09-25) - Enumerations
 - Create test for enums, fix enums and MANY other fixes
 - merge

## Version 1.1.0 (2012-09-19) - Python3
 - Full python3 compatability built in
 - fix warnings in setup.py
 - fix usage test
 - Modify the mechanisms for internal communication to not convert strings so much.
 - Make sure the tests pass.
 - Add usage and improve compat testing
 - Add usage and improve compat testing
 - Update changelog

## Version 1.0.0 (2012-08-17) - New API
 - Bump version because of new api
 - Improve testing and api

## Version 0.9.7 (2012-08-15) - Older UNIX
 - Add in support for older unix machines thanks to Jay Sigbrandt for bring the problem to attention.
 - Fixed empty crontab bug, thanks to James.

## Version 0.9.6 (2010-12-17) - Fixes
 - Update with a new text.

## Version 0.9.5 (2010-10-20) - Net entries
 - Fix weird issue with making new entries.

## Version 0.9.4 (2010-02-20) - Find command
 - Update to latest
 - Update changelog

## Version 0.9.3 (2009-09-18) - Returns
 - Make sure the crontab has a CR at the end.

## Version 0.9.2 (2009-07-07) - Parse spaced entries
 - Make sure we can parse spaced entries

## Version 0.9.1 (2009-07-07) - Import to bzr
 - Inital import to bzr
