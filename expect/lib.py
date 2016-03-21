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

def trace_route(spawn, target_router_name):
    print('Tracing route to %s' % target_router_name)
    target_ip = loopback_ips[target_router_name]
    spawn.send('traceroute %s\r' % target_ip)
    spawn.expect('VRF info:')
