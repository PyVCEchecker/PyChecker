import os
import stat

from exabgp.environment import ROOT


def socket_location(pipename='exabgp'):
    locations = [
        '/run/exabgp/',
        '/run/%d/' % os.getuid(),
        '/run/',
        '/var/run/exabgp/',
        '/var/run/%d/' % os.getuid(),
        '/var/run/',
        ROOT + '/run/exabgp/',
        ROOT + '/run/%d/' % os.getuid(),
        ROOT + '/run/',
        ROOT + '/var/run/exabgp/',
        ROOT + '/var/run/%d/' % os.getuid(),
        ROOT + '/var/run/',
    ]
    for location in locations:
        socket = location + pipename

        try:
            if not stat.S_ISSOCK(os.stat(socket).st_mode):
                continue
        except Exception:
            continue
        os.environ['exabgp_socket'] = location
        return [location]
    return locations
