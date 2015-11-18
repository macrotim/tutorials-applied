import pytest
from mock import patch
from person import Person, Pet

@pytest.mark.xfail
@patch('person.Pet')
def test_bad(mock_pet):
    mock_pet.noise.return_value = "Meoow" # Wrong.
    person = Person()
    assert person.pet.noise() == "Meoow"

@patch('person.Pet')
def test_good(mock_pet):
    mock_pet.return_value.noise.return_value = "Meoow" # Better.
    person = Person()
    assert person.pet.noise() == "Meoow"
