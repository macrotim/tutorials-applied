""" If you want to promote an implicit binding to be an explicit binding, you
    can annotate the corresponding class with @inject(). The @inject() decorator
    lets you create explicit bindings without needing to create binding specs, as
    long as you can live with the binding defaults (e.g., no annotations on args,
    see below).

    Run with py.test.
    """

import pinject
import pytest

class ExplicitlyBoundClass(object):
    @pinject.inject()
    def __init__(self, foo):
        self.foo = foo

class ImplicitlyBoundClass(object):
    def __init__(self, foo):
        self.foo = foo

class SomeBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_instance='explicit-foo')

def test():
    obj_graph = pinject.new_object_graph(
        binding_specs=[SomeBindingSpec()],
        only_use_explicit_bindings=True)
    with pytest.raises(pinject.NonExplicitlyBoundClassError):
        obj_graph.provide(ImplicitlyBoundClass)

    some_class = obj_graph.provide(ExplicitlyBoundClass)
    assert some_class.foo
