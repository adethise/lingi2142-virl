#!/usr/bin/python3

import pexpect

from lib import *
from config import *

def __main__():
    print()
    print('####################################')
    print('# Test: interfaces for each router #')
    print('####################################')
    test_interfaces()

def test_interfaces():
    routers = sorted(list(telnet_ports))
    for router in routers:
        print("\nAsserting intefaces status for %s" % router)
        interface_count = len(interface_ips[router])+2 # +2 for admin+loopback
        spawn = telnet_to_router(router)
        spawn.sendline('show ip int brief')
        spawn.expect('Interface')
        for _ in range(interface_count):
            spawn.expect(r'\A.*?\n(.+?)\s.+?YES.+?up.+?up')
            print(spawn.match.group(1).decode().ljust(25), end='')
            print("Success")

if __name__ == "__main__":
    __main__()
