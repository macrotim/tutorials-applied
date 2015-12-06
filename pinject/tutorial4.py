""" Pinject creates implicit bindings for classes, but sometimes the implicit
    bindings aren't what you want. For instance, if you have
    SomeReallyLongClassName, you may not want to name your initializer args
    some_really_long_class_name but instead use something shorter like long_name,
    just for this class.

    Run with py.test.
    """

import pinject

class SomeClass(object):
    def __init__(self, long_name):
        self.long_name = long_name

class SomeReallyLongClassName(object):
    def __init__(self):
        self.foo = 'foo'

class MyBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('long_name', to_class=SomeReallyLongClassName)

def test():
    obj_graph = pinject.new_object_graph(binding_specs=[MyBindingSpec()])
    some_class = obj_graph.provide(SomeClass)
    assert some_class.long_name.foo == 'foo'
    assert isinstance(some_class.long_name, SomeReallyLongClassName)
