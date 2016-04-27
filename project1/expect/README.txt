LINGI2142
Group H
2016-03-22

About the tests:
- Requires Python 3.3+ and the pexpect module
- Since the telnet port number change at each startup, you HAVE TO EDIT the config.py
and enter the correct ports number for each router before running any test. The port 
number for each router appears in the homepage of the simulation on the VIRL server. 
- Sometimes the first telnet connection to a router fails for no apparent reason and thus
leads to failures in the tests. Our solution is to spam a few "ping.py" tests in order to
"wake up" all routers before running the full test suite via "test.py". At each new run
of the "ping.py" test, you should see more routers passing the test until they are all ready.
(We will investigate for a cleaner solution the second project).

We have 5 test suites that can be run independently:
- interface.py
- ping.py
- traceroute.py
- routes.py
- deflections.py

Note that tests.py will run all the tests in order.