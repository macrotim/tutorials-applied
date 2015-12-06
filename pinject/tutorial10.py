""" Bindings have precedence: explicit bindings take precedence over implicit bindings.

    Tim: pinject considers SomeClass.foo and Foo to be implicit bindings while
    definitions within configure() to be explicit.
    """

import pinject

class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo

class Foo(object):
    pass

class SomeBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_instance='foo-instance')

obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class = obj_graph.provide(SomeClass)
print some_class.foo
