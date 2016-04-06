#!/usr/bin/python3

import pexpect
import time

from lib import *
from config import *

ips = interface_ips

def __main__():
    print()
    print('###########################################################')
    print('# Test: traceroute from E2 to E1 : E2->C2->E3->C3->C1->E1 #')
    print('###########################################################')
    traceroute_from_Ext2()
    
def traceroute_from_Ext2():
    print('\nAsserting routes from Ext2 for project two part one...')
    ext2 = telnet_to_router(EXT2)

    expect_route(ext2, EXT2, EXT1+EXT3, [
        ips[E2][SW],
        ips[C2][SW],
        ips[E3][SW],
        ips[C3][EAST],
        ips[C1][NE],
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])


if __name__ == "__main__":
    __main__()
