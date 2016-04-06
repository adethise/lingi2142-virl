#!/usr/bin/python3

import pexpect

from lib import *
from config import *

def __main__():
    print()
    print('#####################')
    print('# Test: deflections #')
    print('#####################')
    ext_ips = external_ips.values()

    for internal_router in sorted(core_routers):
        print('\nAsserting deflections from %s' % internal_router)
        src = telnet_to_router(internal_router)

        for external_router_ip in sorted(external_ips.values()):
            print('\tAsserting deflection to %s...'.ljust(35) % external_router_ip, end='')

            # Get next hop to external prefix
            src.sendline('show ip route %s' % external_router_ip)
            src.expect(r'.*\*\s(.*), from')
            via_loopback_addr = src.match.group(1).decode('utf-8')
            src.expect('%s>' % internal_router)

            # Get router name from next hop IP
            router_name = ''
            for name, loopback_ip in loopback_ips.items():
                if loopback_ip == via_loopback_addr:
                    router_name = name

            # Assert that one of the interfaces appears in the traceroute
            send_traceroute_cmd_to_ip(src, external_router_ip)
            try:
                src.expect(list(interface_ips[router_name].values()))
                print('Success')
            except:
                print('Failure')

            src.expect('%s>' % internal_router)

if __name__ == "__main__":
    __main__()
