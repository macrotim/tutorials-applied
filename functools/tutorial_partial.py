"""functools.partial."""

import functools
from util import show_details2 as show_details

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print '\tcalled myfunc with:', (a, b)
    return

if __name__ == '__main__':
    show_details('myfunc', myfunc)
    myfunc('a', 3)
    print

    # Apply functools.partial, which transforms myfunc.
    # Also known as function-currying.
    p1 = functools.partial(myfunc, b=4)
    show_details('partial with named default', p1, True)
    p1('default a')
    p1('override b', b=5)
    print

    # Same idea as above.
    p2 = functools.partial(myfunc, 'default a', b=99)
    show_details('partial with defaults', p2, True)
    p2()
    p2(b='override b')
    print

    # 'Insufficient arguments': p1 expects at least one arg, "a".
    # p1()
