""" Timeouts are a constraint on the runtime of a block of code or a Greenlet.
    Active Greenlets are killed when the Timeout expires.
    """

import gevent
from gevent import Timeout

seconds = 10

timeout = Timeout(1)
timeout.start()

def wait():
    gevent.sleep(10)

try:
    gevent.spawn(wait).join()
except Timeout:
    print('Could not complete')
