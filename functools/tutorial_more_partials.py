"""By defining __call__, MyClass is callable which allows
functools.partial to wrap instances of MyClass."""

import functools

class MyClass(object):
    """Demonstration class for functools"""

    def meth1(self, a, b=2):
        """Docstring for meth1()."""
        print '\tcalled meth1 with:', (self, a, b)
        return

    def meth2(self, c, d=5):
        """Docstring for meth2"""
        print '\tcalled meth2 with:', (self, c, d)
        return

    # Wrap method meth2 overriding "c".
    wrapped_meth2 = functools.partial(meth2, 'wrapped c')
    functools.update_wrapper(wrapped_meth2, meth2)

    def __call__(self, e, f=6):
        """Docstring for MyClass.__call__"""
        print '\tcalled object with:', (self, e, f)
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
    return

o = MyClass()

# Work on meth1.
show_details('meth1 straight', o.meth1)
o.meth1('no default for a', b=3)
print

p1 = functools.partial(o.meth1, b=4)
functools.update_wrapper(p1, o.meth1)
show_details('meth1 wrapper', p1)
p1('a goes here')
print

# Work on meth2.
show_details('meth2', o.meth2)
o.meth2('no default for c', d=6)
print

# Work on wrapped_meth2.
show_details('wrapped meth2', o.wrapped_meth2)
o.wrapped_meth2('no default for c', d=6)
print

# The object instance defines __call__ and is callable.
show_details('instance', o)
o('no default for e')
print

p2 = functools.partial(o, f=7)
show_details('instance wrapper', p2)
p2('e goes here')
