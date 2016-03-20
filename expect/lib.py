import pexpect
import sys

from config import *

def telnet_to_router(router_name):
    port = telnet_ports[router_name]
    child = pexpect.spawn('telnet %s %s' % (telnet_ip, port), timeout=1)
    print('Connected to %s' % router_name)
    return child

def trace_route(spawn, target_router_name):
    print('Tracing route to %s' % target_router_name)
    target_ip = loopback_ips[target_router_name]
    spawn.send('traceroute %s' % target_ip)
