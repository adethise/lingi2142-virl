#!/usr/bin/python3

import pexpect
import time

from lib import *
from config import *

ips = interface_ips

def __main__():
    print()
    print('####################################')
    print('# Test: traceroute for each router #')
    print('####################################')
    print()
    # traceroute_from_Ext1()
    # traceroute_from_Ext2()
    # traceroute_from_Ext3()
    # traceroute_from_E1()
    # traceroute_from_E2()
    traceroute_from_E3()

def traceroute_from_Ext1():
    print('Asserting routes from Ext1...\n')
    ext1 = telnet_to_router(EXT1)

    expect_route(ext1, EXT1, EXT3, [
        ips[E1][NORTH],
        ips[C1][NW],
        ips[E2][NW],
        ips[EXT3][EAST]
    ])
    expect_route(ext1, EXT1, EXT2, [
        ips[E1][NORTH],
        ips[C1][NW],
        ips[C3][SW],
        ips[E3][WEST],
        ips[EXT2][SOUTH]
    ])
    expect_route(ext1, EXT1, C2, [
        ips[E1][NORTH],
        ips[C1][NW],
        ips[C3][SW],
        ips[C2][NW]
    ])

def traceroute_from_Ext2():
    print('Asserting routes from Ext2...\n')
    ext2 = telnet_to_router(EXT2)

    expect_route(ext2, EXT2, EXT1, [
        ips[E3][NORTH],
        ips[C3][EAST],
        ips[C1][NE],
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])
    expect_route(ext2, EXT2, EXT3, [
        ips[E3][NORTH],
        ips[C2][NE],
        ips[E2][NE],
        ips[EXT3][EAST]
    ])

def traceroute_from_Ext3():
    print('Asserting routes from Ext3...\n')
    ext3 = telnet_to_router(EXT3)

    expect_route(ext3, EXT3, EXT1, [
        ips[E2][SW],
        ips[C1][SE],
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])
    expect_route(ext3, EXT3, EXT2, [
        ips[E2][SW],
        ips[C2][SW],
        ips[E3][SW],
        ips[EXT2][SOUTH]
    ])

def traceroute_from_E1():
    print('Asserting routes from E1...\n')
    e1 = telnet_to_router(E1)

    expect_route(e1, E1, EXT3, [
        ips[C1][NW],
        ips[E2][NW],
        ips[EXT3][EAST]
    ])
    expect_route(e1, E1, EXT2, [
        ips[C1][NW],
        ips[C3][SW],
        ips[E3][WEST],
        ips[EXT2][SOUTH]
    ])
    expect_route(e1, E1, C2, [
        ips[C1][NW],
        ips[C3][SW],
        ips[C2][NW]
    ])

def traceroute_from_E2():
    print('Asserting routes from E2...\n')
    e2 = telnet_to_router(E2)

    expect_route(e2, E2, EXT1, [
        ips[C1][SE],
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])
    expect_route(e2, E2, EXT2, [
        ips[C2][SW],
        ips[E3][SW],
        ips[EXT2][SOUTH]
    ])


def traceroute_from_E3():
    print('Asserting routes from E3...\n')
    e3 = telnet_to_router(E3)

    expect_route(e3, E3, EXT1, [
        ips[C3][EAST],
        ips[C1][NE],
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])
    expect_route(e3, E3, EXT3, [
        ips[C2][NE],
        ips[E2][NE],
        ips[EXT3][EAST]
    ])

__main__()
