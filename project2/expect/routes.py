#!/usr/bin/python3

import pexpect

from config import *

WHITE = r'\s*'
NUM = r'\d{1,3}'

def __main__():
    connexions = [(telnet_ip, telnet_ports[n], n) for n in sorted(telnet_ports.keys())]

    print()
    print('###############################')
    print('# Test: border routers tables #')
    print('###############################')
    print()

    success= True
    tests = [route_table_E1, route_table_E2, route_table_E3]
    for test in tests:
        success = test() and success

    if success:
        print('ROUTES: Test successful')
    else:
        print('ROUTES: One or more tests failed')
    del success


def check_result(ospf, loop, border):
    correct = True

    if not border:
        print('Missing outgoing routes.')
        correct = False
    if loop < 6:
        print('Missing loopback addresses.')
        correct = False
    if ospf == 0:
        print('Missing OSPF addresses.')
        correct = False

    if correct:
        print('Test successful')
    else:
        print('Test failed')

    print()
    return correct


def route_table_E1():
    name = E1
    telnet_port = telnet_ports[name]
    telnet_info = (telnet_ip, telnet_port, name)
    print('Testing route table from connexion telnet://%s:%s (%s)' % telnet_info)

    child = pexpect.spawn('telnet %s %s' % (telnet_ip, telnet_port))
    child.logfile = open('log.txt', 'ab')

    try:
        expected = [
                # prompt
                r'E1>',
                # static routes
                r'S%s 10.0.0.0/16 is directly connected, Null0'
                        % (WHITE),
                # external routes
                r'B%s 10.1.0.0/16 .*? via 10.1.0.1' 
                        % (WHITE),
                r'C%s 10.1.0.0/30 is directly connected, GigabitEthernet0/2'
                        % (WHITE),
                r'B%s 10.4.0.0/16 .*? via 10.1.0.1' 
                        % (WHITE),
                # internal routes
                r'O%s 10.0.%s.%s/%s'
                        % (WHITE, NUM, NUM, NUM),
                # loopback routes
                r'[COB]%s 192.168.%s.%s/32' 
                        % (WHITE, NUM, NUM),
                r'--More--'
        ]

        ospf = 0
        loop = 0
        border_prefix = False
        border_prefix_common = False
        border_router = False
        started = False

        idx = -1
        child.expect([r'Connected to %s' % telnet_ip])
        child.expect([r'Escape character is'])
        child.expect([r'\r\n'])
        child.sendline('')

        print('Connexion established...')

        child.expect(r'E1>')
        child.sendline('show ip route')

        while idx != 0 or not started:
            idx = child.expect(expected)

            if idx != 0:
                started = True

            if idx == 1:
                print('\tFound AS10 static prefix: '.ljust(35)
                        + str(child.after.decode()[8:]))
            elif idx == 2:
                print('\tFound AS1 prefix: '.ljust(35)
                        + str(child.after.decode()[8:]))
                border_prefix = True
            elif idx == 3:
                print('\tFound AS1 border router address: '.ljust(35) 
                        + str(child.after.decode()[8:]))
                border_router = True
            elif idx == 4:
                print('\tFound AS4 prefix: '.ljust(35)
                        + str(child.after.decode()[8:]))
                border_prefix_common = True
            elif idx == 5:
                print('\tFound OSPF address: '.ljust(35)
                        + str(child.after.decode()[8:]))
                ospf += 1
            elif idx == 6:
                print('\tFound loopback address: '.ljust(35)
                        + str(child.after.decode()[8:]))
                loop += 1
            elif idx == 7:
                child.send(' ')

        del child

        print('Found %d addresses collected from OSPF.' % ospf)
        print('Found %d loopback addresses.' % loop)
        
        border = border_prefix and border_prefix_common and border_router
        return check_result(ospf, loop, border)


    except (pexpect.EOF, pexpect.TIMEOUT):
        print('Test failed')
        return False


def route_table_E2():
    name = E2
    telnet_port = telnet_ports[name]
    telnet_info = (telnet_ip, telnet_port, name)
    print('Testing route table from connexion telnet://%s:%s (%s)' % telnet_info)

    child = pexpect.spawn('telnet %s %s' % (telnet_ip, telnet_port))
    child.logfile = open('log.txt', 'ab')

    try:
        expected = [
                # prompt
                r'E2>',
                # static routes
                r'S%s 10.0.0.0/16 is directly connected, Null0'
                        % (WHITE),
                # external routes
                r'B%s 10.2.0.0/16 .*? via 10.2.0.1' 
                        % (WHITE),
                r'C%s 10.2.0.0/30 is directly connected, GigabitEthernet0/3'
                        % (WHITE),
                r'B%s 10.4.0.0/16 .*? via 10.2.0.1' 
                        % (WHITE),
                # internal routes
                r'O%s 10.0.%s.%s/%s'
                        % (WHITE, NUM, NUM, NUM),
                # loopback routes
                r'[COB]%s 192.168.%s.%s/32' 
                        % (WHITE, NUM, NUM),
                r'--More--'
        ]

        ospf = 0
        loop = 0
        border_prefix = False
        border_prefix_common = False
        border_router = False
        started = False

        idx = -1
        child.expect([r'Connected to %s' % telnet_ip])
        child.expect([r'Escape character is'])
        child.expect([r'\r\n'])
        child.sendline('')

        print('Connexion established...')

        child.expect(r'E2>')
        child.sendline('show ip route')

        while idx != 0 or not started:
            idx = child.expect(expected)

            if idx != 0:
                started = True

            if idx == 1:
                print('\tFound AS10 static prefix: '.ljust(35)
                        + str(child.after.decode()[8:]))
            elif idx == 2:
                print('\tFound AS2 prefix: '.ljust(35)
                        + str(child.after.decode()[8:]))
                border_prefix = True
            elif idx == 3:
                print('\tFound AS2 border router address: '.ljust(35) 
                        + str(child.after.decode()[8:]))
                border_router = True
            elif idx == 4:
                print('\tFound AS4 prefix: '.ljust(35)
                        + str(child.after.decode()[8:]))
                border_prefix_common = True
            elif idx == 5:
                print('\tFound OSPF address: '.ljust(35)
                        + str(child.after.decode()[8:]))
                ospf += 1
            elif idx == 6:
                print('\tFound loopback address: '.ljust(35)
                        + str(child.after.decode()[8:]))
                loop += 1
            elif idx == 7:
                child.send(' ')

        del child

        print('Found %d addresses collected from OSPF.' % ospf)
        print('Found %d loopback addresses.' % loop)
        
        border = border_prefix and border_prefix_common and border_router
        return check_result(ospf, loop, border)

    except (pexpect.EOF, pexpect.TIMEOUT):
        print('Test failed')
        return False


def route_table_E3():
    name = E3
    telnet_port = telnet_ports[name]
    telnet_info = (telnet_ip, telnet_port, name)
    print('Testing route table from connexion telnet://%s:%s (%s)' % telnet_info)

    child = pexpect.spawn('telnet %s %s' % (telnet_ip, telnet_port))
    child.logfile = open('log.txt', 'wb')

    try:
        expected = [
                # prompt
                r'E3>',
                # static routes
                r'S%s 10.0.0.0/16 is directly connected, Null0'
                        % (WHITE),
                # external routes
                r'B%s 10.3.0.0/16 .*? via 10.3.0.1' 
                        % (WHITE),
                r'C%s 10.3.0.0/30 is directly connected, GigabitEthernet0/3'
                        % (WHITE),
                r'B%s 10.4.0.0/16 .*? via 10.3.0.1' 
                        % (WHITE),
                # internal routes
                r'O%s 10.0.%s.%s/%s'
                        % (WHITE, NUM, NUM, NUM),
                # loopback routes
                r'[COB]%s 192.168.%s.%s/32' 
                        % (WHITE, NUM, NUM),
                r'--More--'
        ]

        ospf = 0
        loop = 0
        border_prefix = False
        border_prefix_common = False
        border_router = False
        started = False

        idx = -1
        child.expect([r'Connected to %s' % telnet_ip])
        child.expect([r'Escape character is'])
        child.expect([r'\r\n'])
        child.sendline('')

        print('Connexion established...')

        child.expect(r'E3>')
        child.sendline('show ip route')

        while idx != 0 or not started:
            idx = child.expect(expected)

            if idx != 0:
                started = True

            if idx == 1:
                print('\tFound AS10 static prefix: '.ljust(35)
                        + str(child.after.decode()[8:]))
            elif idx == 2:
                print('\tFound AS3 prefix: '.ljust(35)
                        + str(child.after.decode()[8:]))
                border_prefix = True
            elif idx == 3:
                print('\tFound AS3 border router address: '.ljust(35) 
                        + str(child.after.decode()[8:]))
                border_router = True
            elif idx == 4:
                print('\tFound AS4 prefix: '.ljust(35)
                        + str(child.after.decode()[8:]))
                border_prefix_common = True
            elif idx == 5:
                print('\tFound OSPF address: '.ljust(35)
                        + str(child.after.decode()[8:]))
                ospf += 1
            elif idx == 6:
                print('\tFound loopback address: '.ljust(35)
                        + str(child.after.decode()[8:]))
                loop += 1
            elif idx == 7:
                child.send(' ')

        del child

        print('Found %d addresses collected from OSPF.' % ospf)
        print('Found %d loopback addresses.' % loop)
        
        border = border_prefix and border_prefix_common and border_router
        return check_result(ospf, loop, border)

    except (pexpect.EOF, pexpect.TIMEOUT):
        print('Test failed')
        return False



if __name__ == "__main__":
    __main__()
