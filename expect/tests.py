#!/usr/bin/python3

import pexpect
import sys


if len(sys.argv) != 3:
    print('USAGE:    %s IP PORT_RANGE' % sys.argv[0])
    print('EXAMPLE:  %s %s %s' % (sys.argv[0], '172.156.58.2', '17000-17010'))
else:
    __main__(sys.argv)



def test_ping(telnet_info, params):
    """
    Test ping to each router.
    @param router = tuple (ip, port) for telnet connexion
    @param params = list of ips to ping
    """

    print('Testing ping from connexion telnet://%s:%s' % telnet_info)

    child = pexpect.spawn('telnet %s %s' % telnet_info, timeout=1)

    try:
        index = child.expect(['uefquqebqoub'])

        print('Connexion established...')

        for ip in params:
            print('\tPinging ip %s... ' % ip, end='')

            child.sendline('ping %s' % ip)
            index = child.expect(['ip success'])


            print('Success')

        print('Closing connexion.\n')

        #child.sendline('exit')
        #child.expect(pexpect.EOF)

        return True

    except (pexpect.EOF, pexpect.TIMEOUT):
        print('Test failed')
        return False
        

def __main__(argv):
    telnet_ip = argv[1]
    (telnet_port_start, telnet_port_end) = map(int, argv[2].split('-'))
    telnet_ports = map(str, range(telnet_port_start, telnet_port_end+1))

    connexions = [(telnet_ip, telnet_port) for telnet_port in telnet_ports]
    routers = ['192.168.0.%d' % d for d in range(10)]

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
