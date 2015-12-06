""" The configure() method of a binding spec also may take a function require()
    as an arg and use that function to require that a binding be present without
    actually defining that binding. require() takes as args the name of the arg for
    which to require a binding.
    """

import pinject
import pytest

class MainBindingSpec(pinject.BindingSpec):
    def configure(self, require):
        require('foo')

class RealFooBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_instance='a-real-foo')

class StubFooBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_instance='a-stub-foo')

class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo

def test():
    obj_graph = pinject.new_object_graph(binding_specs=[MainBindingSpec(), RealFooBindingSpec()])
    some_class = obj_graph.provide(SomeClass)
    assert some_class.foo == 'a-real-foo'

    with pytest.raises(pinject.MissingRequiredBindingError):
        pinject.new_object_graph(binding_specs=[MainBindingSpec()])

    obj_graph = pinject.new_object_graph(binding_specs=[MainBindingSpec(), StubFooBindingSpec()])
    some_class = obj_graph.provide(SomeClass)
    assert some_class.foo == 'a-stub-foo'
