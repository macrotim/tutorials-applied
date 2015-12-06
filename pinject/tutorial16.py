""" Every binding is associated with a scope. You can specify a scope for a
    binding by decorating a provider method with @in_scope(), or by passing an
    in_scope arg to bind() in a binding spec's configure() method.
    """

import pinject

class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo

class SomeBindingSpec(pinject.BindingSpec):
    @pinject.provides(in_scope=pinject.PROTOTYPE)
    def provide_foo(self):
        return object()

obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class_1 = obj_graph.provide(SomeClass)
some_class_2 = obj_graph.provide(SomeClass)
print some_class_1.foo is some_class_2.foo


