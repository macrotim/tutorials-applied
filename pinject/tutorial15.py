""" By default, Pinject remembers the object it injected into a (possibly
    annotated) arg, so that it can inject the same object into other args
    with the same name.
    """

import pinject

class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo

class SomeBindingSpec(pinject.BindingSpec):
    def provide_foo(self):
        return object()

obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class_1 = obj_graph.provide(SomeClass)
some_class_2 = obj_graph.provide(SomeClass)
print some_class_1.foo is some_class_2.foo
