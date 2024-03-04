from tests import compatibility_issues

## PRIVATE CALDAV SERVER(S) TO RUN TESTS TOWARDS
## Make a list of your own servers/accounts that you'd like to run the
## test towards.  Running the test suite towards a personal account
## should generally be safe, it should not mess up with content there
## and it should clean up after itself, but don't sue me if anything
## goes wrong ...

caldav_servers = [
    {
        ## This is all that is really needed - url, username and
        ## password.  The username and password may also be passed in
        ## the URL itself (like
        ## https://sam_i_am:hunter2@server.example.ccom/)
	#'url': 'https://p62-caldav.icloud.com/17134649682/calendars',
        'url': 'https://caldav.icloud.com/',
        'username': 'nylastest002@icloud.com',
        'password': 'cijw-aiab-xiea-vfff',

	## skip ssl cert verification, for self-signed certificates
	## (sort of moot nowadays with letsencrypt freely available)
        #'ssl_cert_verify': False

        ## For tests - lists what tests should be skipped due to incompatibility issues
        'incompatibilities': compatibility_issues.icloud
    }]
caldav_servers.append({'url': "https://www.google.com/calendar/dav/", "password": "suck google froobar", "username": "tobixen@gmail.com", 'incompatibilities': compatibility_issues.google})
caldav_servers.append({'password': "/family.", "url": "http://calendar.bekkenstenveien53c.oslo.no/caldav.php/", "username": "tobias", 'incompatibilities': compatibility_issues.davical + [ 'no_freebusy_rfc4791' ]})
#caldav_servers.append({'url': 'https://cal-dev.dfn.de/pwdavical/caldav.php/', 'username': 'pycaldav', 'password': 'pycaldav', 'incompatibilities': compatibility_issues.davical})
#caldav_servers.append({'url': 'https://zimbra.redpill-linpro.com/dav/', 'username': 'tobias@redpill-linpro.com', 'password': '/r3g3l3n3@Zimbra.', 'incompatibilities': compatibility_issues.zimbra})
#caldav_servers.append({'url': 'https://demo.sogo.nu/SOGo/dav/', 'username': 'sogo1', 'password': 'sogo1', 'incompatibilities': []})

#rfc6638_users = [ caldav_servers[4], ]
#sogo = caldav_servers[-1].copy()

#rfc6638_users = [ caldav_servers[3], caldav_servers[0] ]

#caldav_servers = [ caldav_servers[1] ]
#caldav_servers = [ ]
if len(caldav_servers) == 1:
    test_xandikos = False
    test_radicale = False

## MASTER SWITCHES FOR TEST SERVER SETUP
## With those configuration switches, pre-configured test servers in conf.py
## can be turned on or off

## test_public_test_servers - Use the list of common public test
## servers from conf.py.  As of 2020-10 no public test servers exists, so this option
## is currently moot :-(
test_public_test_servers = False

## test_private_test_servers - test using the list configured above in this file.
test_private_test_servers = True

## test_xandikos and test_radicale ... since the xandikos and radicale caldav server implementation is
## written in python and can be instantiated quite easily, those will
## be the default caldav implementation to test towards.

## DEPRECATED - only_private is superceded by test_public_servers,
## left here for backward-compatibility.
#only_private=False
