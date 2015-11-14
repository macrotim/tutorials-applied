"""functools.update_wrapper"""

import functools
from util import show_details

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print '\tcalled myfunc with:', (a, b)
    return

# myfunc is a standard function.
show_details('myfunc', myfunc)

# p1 is missing the attribute __name__.
p1 = functools.partial(myfunc, b=4)
show_details('raw wrapper', p1)

print 'Updating wrapper:'
print '\tassign:', functools.WRAPPER_ASSIGNMENTS
print '\tupdate:', functools.WRAPPER_UPDATES
print

# Copy attributes to the wrapper as defined by the constants above.
functools.update_wrapper(p1, myfunc)
show_details('updated wrapper', p1)
