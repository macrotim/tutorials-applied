"""The real power of gevent comes when we use it for network and IO bound
   functions which can be cooperatively scheduled. Gevent has taken care of
   all the details to ensure that your network libraries will implicitly
   yield their greenlet contexts whenever possible.
   """

import time
import gevent
from gevent import select

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)

def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print('Started Polling: %s' % tic())
    select.select([], [], [], 3) # Tim: Block this greenlet until the events are ready,
                                 #      but no events are specified so block forever,
                                 #      or until the timeout of 3 seconds expires.
    print('Ended Polling: %s' % tic())

def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print('Started Polling: %s' % tic())
    select.select([], [], [], 3)
    print('Ended Polling: %s' % tic())

def gr3():
    print("Hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)

gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
])
