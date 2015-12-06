""" Pinject injects all args of provider methods that have no default when it
    calls the provider method.
    """

import pinject

class SomeClass(object):
    def __init__(self, foobar):
        self.foobar = foobar

class SomeBindingSpec(pinject.BindingSpec):
    def provide_foobar(self, bar, hyphen='-'):
        return 'foo' + hyphen + bar
    def provide_bar(self):
        return 'bar'

obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class = obj_graph.provide(SomeClass)
print some_class.foobar
