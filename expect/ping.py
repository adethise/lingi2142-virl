#!/usr/bin/python3

import pexpect

def ping_from(ip, port, to):
    child = pexpect.spawn('telnet %s %s' % (ip, port))
    child.expect('?')
    for (ip, port) in to:
        child.sendline('ping %s %s' % (ip, port))
        child.expect('? ip success')
    child.sendline('exit')
    #child.expect_finished()


ip = '172.90.0.1'
to = ['192.168.0.%d' % d for d in range(0,10)]

for p in range(17000, 17010):
    ping_from(ip, str(p), to)
