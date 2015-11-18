from mock import patch
patch('decorators.noise_logger', lambda x: x).start()
from person import Person

def test_decorator():
    person = Person()
    assert person.pet.noise() == "Woof"
