import pytest
from mock import patch
from person import Person

@pytest.mark.xfail
@patch('person.noise_logger', lambda x: x)
def test_decorator():
    person = Person()
    assert person.pet.noise() == "Woof"
