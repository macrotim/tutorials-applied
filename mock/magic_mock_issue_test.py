"""Here, I isolate an issue that I spent some time stuck on.
   Mock.assert_called_with failed unexpectedly when used in a certain way.

   Use py.test to run the test.
   """

import unittest

from mock import MagicMock

class MockTest(unittest.TestCase):

    def test_fails(self):
        with self.assertRaises(AssertionError):
            Request = MagicMock()
            request = Request()
            request.get('http://')
            Request.get.assert_called_with('http://')

    def test_passes(self):
        Request = MagicMock()
        Request.return_value = Request  # The fix/hack.
        request = Request()
        request.get('http://')
        Request.get.assert_called_with('http://')
