import pytest
from mock import patch
from person import Person

@pytest.mark.xfail
@patch('data_source.get_name') # This won't work as expected!
def test_name_bad(mock_get_name):
    mock_get_name.return_value = "Bob"
    person = Person()
    name = person.name()
    assert name == "Bob"

@patch('person.get_name') # Better.
def test_name_good(mock_get_name):
    mock_get_name.return_value = "Bob"
    person = Person()
    name = person.name()
    assert name == "Bob"
