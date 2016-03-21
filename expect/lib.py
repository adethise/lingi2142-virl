import pexpect
import sys
import time

from config import *

def telnet_to_router(router_name):
    port = telnet_ports[router_name]
    print('telnet %s %s' % (telnet_ip, port))
    spawn = pexpect.spawn('telnet %s %s' % (telnet_ip, port), timeout=1)
    spawn.expect([r'Connected to %s' % telnet_ip])
    spawn.sendline('')
    log = open("log.txt","wb")
    spawn.logfile = log
    spawn.expect('%s>' % router_name)
    print('Connected to %s' % router_name)
    return spawn

def send_traceroute_cmd(spawn, target_router):
    target_ip = loopback_ips[target_router]
    spawn.send('traceroute %s\r' % target_ip)
    spawn.expect('VRF info:')

def expect_route(spawn, router_from, router_dst, hops):
    print('Asserting traceroute from %s to %s' % (router_from, router_dst))
    print('Expecting: %s', '-'.join(hops))
    send_traceroute_cmd(spawn, router_dst)
    for hop in hops:
        spawn.expect(hop)
    print('Pass')
