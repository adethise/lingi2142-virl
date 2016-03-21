import pexpect
import time

from lib import *
from config import *

e1 = telnet_to_router(C1)
trace_route(e1, E3)
