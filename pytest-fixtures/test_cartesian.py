"""I produce a cartesian product using fixture params. Given two first
   names and two last names, we get four full names.

   The cartesian can be useful for testing a variety of configurations
   for, for example, Flask.

   All four tests are intended to fail.
   """

import pytest

@pytest.fixture(params=['Brad', 'Angelina'])
def first_name(request):
    return request.param

@pytest.fixture(params=['Pitt', 'Jolie'])
def full_name(first_name, request):
    return ' '.join([first_name, request.param])

def test_name(full_name):
    assert full_name == None
