""" """

import pinject
import pytest

class MainBindingSpec(pinject.BindingSpec):
    def configure(self, require):
        require('foo', annotated_with='annot')

class NonSatisfyingBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_instance='an-unannotated-foo')

class SatisfyingBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', annotated_with='annot', to_instance='an-annotated-foo')

def test_good():
    obj_graph = pinject.new_object_graph(
        binding_specs=[MainBindingSpec(), SatisfyingBindingSpec()])

def test_bad():
    with pytest.raises(pinject.MissingRequiredBindingError):
        obj_graph = pinject.new_object_graph(
            binding_specs=[MainBindingSpec(),
                           NonSatisfyingBindingSpec()])  # would raise a MissingRequiredBindingError
