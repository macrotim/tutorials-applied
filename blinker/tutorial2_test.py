"""An exercise in unit testing blinker-based code.
   Run the test with py.test.
   """

import unittest
from mock import patch

from tutorial2 import send_data

@patch('tutorial2.receive_data')
class SendTest(unittest.TestCase):
    def test_send_kwargs(self, receive_data_mock):
        result = send_data.send('anonymous', abc=123)
        receive_data_mock.assert_called_with('anonymous', abc=123)

    def test_send_int(self, receive_data_mock):
        result = send_data.send(1)
        receive_data_mock.assert_called_with(1)

    def test_send_list(self, receive_data_mock):
        result = send_data.send([3, 1, 4])
        receive_data_mock.assert_called_with([3, 1, 4])

    def test_send_no_args(self, receive_data_mock):
        """Blinker sends no-args as None."""
        result = send_data.send()
        receive_data_mock.assert_called_with(None)
