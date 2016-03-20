#!/usr/bin/python3

import pexpect
import sys


def __main__(argv):
    telnet_ip = argv[1]
    telnet_ports = argv[2].split(',')

    connexions = [(telnet_ip, telnet_port) for telnet_port in telnet_ports]
    routers = ['192.168.0.%d' % d for d in range(1, 10)]

    ##############
    # Test: ping #
    ##############

    print()
    print('##########################')
    print('# Test: ping each server #')
    print('##########################')
    print()

    success= True
    for connexion in connexions:
        success= test_ping(connexion, routers) and success

    if success:
        print('PING: Test successful')
    else:
        print('PING: One or more tests failed')
    del success

    #############
    # Test: ... #
    #############


def test_ping(telnet_info, params):
    """
    Test ping to each router.
    @param router = tuple (ip, port) for telnet connexion
    @param params = list of ips to ping
    """

    print('Testing ping from connexion telnet://%s:%s' % telnet_info)

    (telnet_ip, telnet_port) = telnet_info
    child = pexpect.spawn('telnet %s %s' % telnet_info)

    error = 0

    try:
        child.expect([r'Connected to %s' % telnet_ip])
        child.expect([r'Escape character is'])
        child.expect([r'\r\n'])
        child.sendline('')

        print('Connexion established...')

        for ip in params:
            child.expect([r'[EC(Ext)]\d>']) # Waiting for prompt

            print('\tPinging ip %s... ' % ip, end='')

            child.sendline('ping %s' % ip)
            child.expect([r'Success rate is '])
            child.expect([r' '])
            rate = int(child.before) # Get the success percentage

            if rate < 50:
                error += 1
                print('Failure')
            else:
                print('Success')

        print('Closing connexion.\n')

        del child
        #child.sendline('exit')
        #child.expect(pexpect.EOF)

        return error == 0

    except (pexpect.EOF, pexpect.TIMEOUT):
        print('Test failed')
        return False
        

###############################################################################


if len(sys.argv) != 3:
    print('USAGE:    %s IP PORT[,PORT...]' % sys.argv[0])
    print('EXAMPLE:  %s %s %s' % (sys.argv[0], '172.156.58.2', '17000,17002,17012'))
else:
    __main__(sys.argv)

