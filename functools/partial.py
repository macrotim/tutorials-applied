"""Raymond Hettinger recommends using functools.partial to rewrite
   a "while True" into a for-loop.

   Video: https://www.youtube.com/watch?v=OSGv2VnC0go
   """

import random
from functools import  partial

def next_num():
    return random.randint(0,10)

# DO.
for i in iter(partial(next_num), 0):
    print i

"""DON'T.

while True:
    i = next_num()
    if i == 0:
        break
    print i
"""

print 'done'
