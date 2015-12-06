""" Also on the binding side, when defining a provider method, you can use the
    @provides() decorator. The decorator lets you pass an annotated_with arg to
    specify the annotation object.
    """

import pinject

class SomeClass(object):
    @pinject.annotate_arg('foo', 'annot')
    def __init__(self, foo):
        self.foo = foo

class SomeBindingSpec(pinject.BindingSpec):
    @pinject.provides('foo', annotated_with='annot')
    def provide_annot_foo(self):
        return 'foo-with-annot'
    @pinject.provides('foo', annotated_with=12345)
    def provide_12345_foo(self):
        return '12345-foo'

def test():
    obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
    some_class = obj_graph.provide(SomeClass)
    assert some_class.foo == 'foo-with-annot'
