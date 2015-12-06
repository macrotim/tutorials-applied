""" Tim: I was curious what happens if you create a circular dependency.
    Would it result in an infinite loop or throw an error?
    No, pinject tolerates it.
    """

import pinject

class ClassOne(object):
   def __init__(self, foo):
       self.foo = foo

class ClassTwo(object):
    def __init__(self, class_one, bar):
        self.foobar = class_one.foo + bar

class BindingSpecOne(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_instance='foo-')

    def dependencies(self):
        return [BindingSpecTwo()]

class BindingSpecTwo(pinject.BindingSpec):
    def configure(self, bind):
        bind('bar', to_instance='-bar')

    def dependencies(self):
        return [BindingSpecOne()]

def test():
    obj_graph = pinject.new_object_graph(binding_specs=[BindingSpecTwo()])
    class_two = obj_graph.provide(ClassTwo)
    assert class_two.foobar == 'foo--bar'
