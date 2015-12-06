""" As you can see, you don't need to tell Pinject how to construct its
    ObjectGraph, and you don't need to put decorators in your code. Pinject
    has reasonable defaults that allow it to work out of the box.
    """

import pinject

class OuterClass(object):
    def __init__(self, inner_class):
        self.inner_class = inner_class

class InnerClass(object):
    def __init__(self):
        self.forty_two = 42

obj_graph = pinject.new_object_graph()
outer_class = obj_graph.provide(OuterClass)
print outer_class.inner_class.forty_two
