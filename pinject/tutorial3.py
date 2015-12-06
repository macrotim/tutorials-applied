""" Pinject provides decorators that you can use to avoid repetitive initializer bodies.

    Run with py.test.
    """

import pinject

class ClassWithTediousInitializer(object):
    @pinject.copy_args_to_internal_fields
    def __init__(self, foo, bar, baz, quux):
        pass

def test():
    cwti = ClassWithTediousInitializer('a-foo', 'a-bar', 'a-baz', 'a-quux')
    assert cwti._foo == 'a-foo'
