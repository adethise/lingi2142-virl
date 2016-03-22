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
    traceroute_from_Ext1()
    traceroute_from_Ext2()
    traceroute_from_Ext3()
    traceroute_from_E1()
    traceroute_from_E2()
    traceroute_from_E3()
    traceroute_from_C1()
    traceroute_from_C2()
    traceroute_from_C3()

def traceroute_from_Ext1():
    print('\nAsserting routes from Ext1...')
    ext1 = telnet_to_router(EXT1)

    expect_route(ext1, EXT1, EXT3, [
        ips[E1][NORTH],
        ips[C1][NW],
        ips[C3][SW],
        ips[E3][WEST],
        ips[EXT3][SOUTH]
    ])
    expect_route(ext1, EXT1, EXT2, [
        ips[E1][NORTH],
        ips[C1][NW],
        ips[E2][NW],
        ips[EXT2][EAST]
    ])
    expect_route(ext1, EXT1, C2, [
        ips[E1][NORTH],
        ips[C1][NW],
        ips[C3][SW],
        ips[C2][NW]
    ])

def traceroute_from_Ext2():
    print('\nAsserting routes from Ext2...')
    ext2 = telnet_to_router(EXT2)

    expect_route(ext2, EXT2, EXT1, [
        ips[E2][SW],
        ips[C1][SE],
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])
    expect_route(ext2, EXT2, EXT3, [
        ips[E2][SW],
        ips[C2][SW],
        ips[E3][SW],
        ips[EXT3][SOUTH]
    ])

def traceroute_from_Ext3():
    print('\nAsserting routes from Ext3...')
    ext3 = telnet_to_router(EXT3)

    expect_route(ext3, EXT3, EXT1, [
        ips[E3][NORTH],
        ips[C3][EAST],
        ips[C1][NE],
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])
    expect_route(ext3, EXT3, EXT2, [
        ips[E3][NORTH],
        ips[C2][NE],
        ips[E2][NE],
        ips[EXT2][EAST]
    ])

def traceroute_from_E1():
    print('\nAsserting routes from E1...')
    e1 = telnet_to_router(E1)

    expect_route(e1, E1, EXT2, [
        ips[C1][NW],
        ips[E2][NW],
        ips[EXT2][EAST]
    ])
    expect_route(e1, E1, EXT3, [
        ips[C1][NW],
        ips[C3][SW],
        ips[E3][WEST],
        ips[EXT3][SOUTH]
    ])
    expect_route(e1, E1, C2, [
        ips[C1][NW],
        ips[C3][SW],
        ips[C2][NW]
    ])

def traceroute_from_E2():
    print('\nAsserting routes from E2...')
    e2 = telnet_to_router(E2)

    expect_route(e2, E2, EXT1, [
        ips[C1][SE],
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])
    expect_route(e2, E2, EXT3, [
        ips[C2][SW],
        ips[E3][SW],
        ips[EXT3][SOUTH]
    ])

def traceroute_from_E3():
    print('\nAsserting routes from E3...')
    e3 = telnet_to_router(E3)

    expect_route(e3, E3, EXT1, [
        ips[C3][EAST],
        ips[C1][NE],
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])
    expect_route(e3, E3, EXT2, [
        ips[C2][NE],
        ips[E2][NE],
        ips[EXT2][EAST]
    ])

def traceroute_from_C1():
    print('\nAsserting routes from C1...')
    c1 = telnet_to_router(C1)

    expect_route(c1, C1, EXT1, [
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])
    expect_route(c1, C1, EXT3, [
        ips[C3][SW],
        ips[E3][WEST],
        ips[EXT3][SOUTH]
    ])
    expect_route(c1, C1, EXT2, [
        ips[E2][NW],
        ips[EXT2][EAST]
    ])

def traceroute_from_C2():
    print('\nAsserting routes from C2...')
    c2 = telnet_to_router(C2)

    expect_route(c2, C2, EXT1, [
        ips[C3][SE],
        ips[C1][NE],
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])
    expect_route(c2, C2, EXT2, [
        ips[E2][NE],
        ips[EXT2][EAST]
    ])
    expect_route(c2, C2, EXT3, [
        ips[E3][SW],
        ips[EXT3][SOUTH]
    ])

def traceroute_from_C3():
    print('\nAsserting routes from C3...')
    c3 = telnet_to_router(C3)

    expect_route(c3, C3, EXT1, [
        ips[C1][NE],
        ips[E1][SE],
        ips[EXT1][SOUTH]
    ])
    expect_route(c3, C3, EXT2, [
        ips[C1][NE],
        ips[E2][NW],
        ips[EXT2][EAST]
    ])
    expect_route(c3, C3, EXT3, [
        ips[E3][WEST],
        ips[EXT3][SOUTH]
    ])

__main__()
