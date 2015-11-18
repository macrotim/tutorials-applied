"""Here, I isolate an issue that I spent some time stuck on.

   It comes down to this:
   - If you mock a class
   - and you instantiate that class
   - and you call method M on that instance
   - and you want to assert M was called
   then, you must set the mock's return_value.

   An alternative is to use dependency injection.

   Use py.test to run the test.
   """

import pytest
import unittest
from mock import patch, MagicMock
from facebook_service import FacebookService

class MockTest(unittest.TestCase):

    @pytest.mark.xfail
    @patch('facebook_service.Request')
    def test_fails(self, RequestMock):
        FacebookService().get_comment(1)
        RequestMock.get.assert_called_with('http://')

    @patch('facebook_service.Request')
    def test_passes(self, RequestMock):
        RequestMock.return_value = RequestMock  # The fix.
        FacebookService().get_comment(1)
        RequestMock.get.assert_called_with('http://')
