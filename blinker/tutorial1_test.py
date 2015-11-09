"""An exercise in unit testing blinker-based code.
   Run the test with py.test.
   """

from mock import patch

from tutorial1 import Processor

@patch('tutorial1.subscriber')
def test_ready(subscriber_mock):
    processor_a = Processor('a')
    processor_a.go()
    subscriber_mock.assert_called_with(processor_a)
