"""Pass both bind and require into configure()."""

import pinject

class MainBindingSpec(pinject.BindingSpec):
    def configure(self, bind, require):
        require('foo')
        bind('foo', to_instance='a-real-foo')

class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo

def test():
    obj_graph = pinject.new_object_graph(binding_specs=[MainBindingSpec()])
    some_class = obj_graph.provide(SomeClass)
    assert some_class.foo == 'a-real-foo'
