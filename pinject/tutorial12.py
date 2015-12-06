""" Pinject annotations let you have different objects injected for the same arg
    name. For instance, you may have two classes in different parts of your codebase
    named the same thing, and you want to use the same arg name in different parts
    of your codebase.
    """

import pinject

class SomeClass(object):
    @pinject.annotate_arg('foo', 'annot')
    def __init__(self, foo):
        self.foo = foo

class SomeBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', annotated_with='annot', to_instance='foo-with-annot')
        bind('foo', annotated_with=12345, to_instance='12345-foo')

obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class = obj_graph.provide(SomeClass)
print some_class.foo
