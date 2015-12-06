""" Using to_instance binds to an instance of some object. Every time the binding
    is used, Pinject uses that instance.

    Run with py.test.
    """

import pinject

class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo

class MyBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_instance={'A': 65, 'B': 66})

def test_to_instance():
    """ Tim: Demonstrate that the same data structure is shared across all
        instances of SomeClass.foo."""

    obj_graph = pinject.new_object_graph(binding_specs=[MyBindingSpec()])
    some_class1 = obj_graph.provide(SomeClass)
    some_class2 = obj_graph.provide(SomeClass)
    some_class1.foo['C'] = 67
    assert some_class2.foo['C'] == 67
