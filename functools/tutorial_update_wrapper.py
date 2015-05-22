"""functools.update_wrapper"""

import functools

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print '\tcalled myfunc with:', (a, b)
    return

def show_details(name, f):
    """Show details of a callable object."""
    print '%s:' % name
    print '\tobject:', f
    print '\t__name__:',
    try:
        print f.__name__
    except AttributeError:
        print '(no __name__)'
    print '\t__doc__', repr(f.__doc__)
    print
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
