#!/usr/bin/python3

import pexpect

from config import *


def __main__():
    connexions = [(telnet_ip, telnet_ports[n], n) for n in sorted(telnet_ports.keys())]

    print()
    print('##########################')
    print('# Test: ping each server #')
    print('##########################')
    print()

    success= True
    for connexion in connexions:
        success= test_ping(connexion, loopback_ips) and success

    if success:
        print('PING: Test successful')
    else:
        print('PING: One or more tests failed')
    del success


def test_ping(telnet_info, params):
    """
    Test ping to each router.
    @param router = tuple (ip, port) for telnet connexion
    @param params = list of ips to ping
    """

    print('Testing ping from connexion telnet://%s:%s (%s)' % telnet_info)

    (telnet_ip, telnet_port, name) = telnet_info
    child = pexpect.spawn('telnet %s %s' % (telnet_ip, telnet_port))

    error = 0

    try:
        child.expect([r'Connected to %s' % telnet_ip])
        child.expect([r'Escape character is'])
        child.expect([r'\r\n'])
        child.sendline('')

        print('Connexion established...')

        for n in sorted(params.keys()):
            child.expect([r'[EC(Ext)]\d>']) # Waiting for prompt

            print(('\tPinging ip %s (%s)... ' % (params[n], n)).ljust(41), end='')

            child.sendline('ping %s' % params[n])
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
        


if __name__ == "__main__":
    __main__()
