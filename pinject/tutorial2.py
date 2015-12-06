""" You may occasionally want to restrict the classes for which new_object_graph()
    creates implicit bindings. If so, new_object_graph() has two args for this
    purpose.

    Run with py.test.
    """

import pinject
import pytest

class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo

class Foo(object):
    pass

def test_run():
    obj_graph = pinject.new_object_graph(modules=None, classes=[SomeClass])
    with pytest.raises(pinject.NothingInjectableForArgError):
        obj_graph.provide(SomeClass)

    obj_graph = pinject.new_object_graph(modules=None, classes=[SomeClass, Foo])
    some_class = obj_graph.provide(SomeClass)
    assert some_class
    assert some_class.foo
