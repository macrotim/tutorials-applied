"""Demonstrate that gevent utilizes only one CPU core."""

import time
import gevent

def compute(n):
    start = time.time()
    while time.time() - start < n:
        pass

start = time.time()
gevent.joinall([
    gevent.spawn(compute, .050),
    gevent.spawn(compute, .050),
    gevent.spawn(compute, .050),
    gevent.spawn(compute, .050)
    ])
elapsed = time.time() - start

print 'Multiple cores would allow this to complete in under 200 milliseconds.'
if elapsed < .200:
    print 'And somehow it did.'
else:
    print 'But of course, gevent utilizes only one CPU core.'
print 'Runtime:', elapsed, 'sec'
