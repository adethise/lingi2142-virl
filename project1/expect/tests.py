#!/usr/bin/python

import interfaces
import ping
import traceroute
import routes
import deflections

interfaces.__main__()
print('\n\n')
ping.__main__()
print('\n\n')
routes.__main__()
print('\n\n')
traceroute.__main__()
print('\n\n')
deflections.__main__()
