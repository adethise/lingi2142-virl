import pexpect
import sys
import time

from config import *

def telnet_to_router(router_name):
    port = telnet_ports[router_name]
    # print('telnet %s %s' % (telnet_ip, port))
    spawn = pexpect.spawn('telnet %s %s' % (telnet_ip, port), timeout=5)
    spawn.expect([r'Connected to %s' % telnet_ip])
    spawn.sendline('')
    log = open("log.txt","wb")
    spawn.logfile = log
    spawn.expect('%s>' % router_name)
    # print('Connected to %s' % router_name)
    return spawn

def send_traceroute_cmd(spawn, target_router):
    send_traceroute_cmd_to_ip(loopback_ips[target_router])

def send_traceroute_cmd_to_ip(spawn, target_ip):
    target_ip = ips[target_router]
    spawn.send('traceroute %s\r' % target_ip)
    spawn.expect('VRF info:')

def expect_route(spawn, router_from, router_dst, hops, hops_alt=None):
    print((('Route to %s' % router_dst).ljust(20) + ('Expecting: %s' % '->'.join(hops)).ljust(70)), end='')
    send_traceroute_cmd(spawn, router_dst)
    if hops_alt == None :
        spawn.expect('.*'.join(hops))
    else :
        spawn.expect(['.*'.join(hops), '.*'.join(hops_alt)])
    spawn.expect('%s>' % router_from)
    print('Success')
