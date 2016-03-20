import pexpect
import time

from lib import *
from config import *

e1 = telnet_to_router(E1)
time.sleep(2)
trace_route(e1, C2)
time.sleep(2)
e1.expect(interface_ips[C1][NW])
e1.expect(interface_ips[C3][SW])
e1.expect(interface_ips[C2][NW])
