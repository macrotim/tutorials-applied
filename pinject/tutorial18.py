"""Pinject creates provider bindings for each bound arg name."""

import pinject

class Foo(object):
  def __init__(self):
    self.forty_two = 42

class SomeBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_class=Foo, in_scope=pinject.PROTOTYPE)

class NeedsProvider(object):
    def __init__(self, provide_foo):
        self.provide_foo = provide_foo

obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
needs_provider = obj_graph.provide(NeedsProvider)
print needs_provider.provide_foo() is needs_provider.provide_foo()
print needs_provider.provide_foo().forty_two
