#!/usr/bin/python3

import pexpect
import time

from lib import *
from config import *

ips = interface_ips

## TODO Add to the network the routers Ext2.1 and Ext2.2 as h1 and h2

def __main__():
    print()
    print('###########################################################')
    print('# Test: traceroute from E2 to E1 : E2->C2->E3->C3->C1->E1 #')
    print('###########################################################')
    traceroute_from_Ext2_1()
    traceroute_from_Ext2_2()
    
def traceroute_from_Ext2_1():
    print('\nAsserting routes from Ext2 for project two part one...')
    ext2 = telnet_to_router(EXT2) # TODO change to Ext2.1

    expect_route(ext2, EXT2, EXT1+EXT3, [
        ips[E2][SW],
        ips[C2][SW],
        ips[E3][SW],
        ips[C3][EAST],
        ips[C1][NE],
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])

def traceroute_from_Ext2_2():
    print('\nAsserting routes from Ext2 for project two part two...')
    ext2 = telnet_to_router(EXT2) # TODO change to Ext2.2

    expect_route(ext2, EXT2, EXT1+EXT3, [
        ips[E2][SW],
        ips[C1][SE],
        ips[C3][SW],
        ips[E3][EAST],
        ips[EXT3][SOUTH]
    ],
    hosts_alt = [
        ips[E2][SW],
        ips[C1][SE],
        ips[C2][WEST],
        ips[C3][SE],
        ips[E3][EAST],
        ips[EXT3][SOUTH]
    ])


if __name__ == "__main__":
    __main__()
