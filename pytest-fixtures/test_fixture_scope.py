"""The fixture's scope attribute tells pytest to invoke the fixture once for every
   function, the current module, or the entire session. This is great for something
   like services that are slow to setup, for example, a Flask instance.
   """

import time
import pytest

@pytest.fixture(scope="function")
def slow_service():
    time.sleep(1)
    return 1

def test_slow1(slow_service):
    assert slow_service == 1

def test_slow2(slow_service):
    assert slow_service == 1
