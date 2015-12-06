"""Memoization of class bindings works at the class level, not at the binding key level. """

import pinject

class InjectedClass(object):
    pass

class SomeObject(object):
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

class SomeBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_class=InjectedClass)
        bind('bar', to_class=InjectedClass)

obj_graph = pinject.new_object_graph(
    binding_specs=[SomeBindingSpec()])
some_object = obj_graph.provide(SomeObject)
print some_object.foo is some_object.bar
