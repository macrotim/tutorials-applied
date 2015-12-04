""" In addition, gevent also provides timeout arguments for a variety of
    Greenlet and data stucture related calls. For example:
    """

import gevent
from gevent import Timeout

time_to_wait = 1 # seconds

class TooLong(Exception):
    pass

with Timeout(time_to_wait, TooLong):
    gevent.sleep(10)
