""" If it takes more to instantiate a class than calling its initializer and
    injecting initializer args, then you can write a provider method for it. Pinject
    can use provider methods to instantiate objects used to inject as the values of
    other args.
    """

import pinject

class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo

class SomeBindingSpec(pinject.BindingSpec):
    def provide_foo(self):
        return 'some-complex-foo'

obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class = obj_graph.provide(SomeClass)
print some_class.foo
