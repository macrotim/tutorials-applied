"""An exercise in unit testing blinker-based code.
   Run the test with py.test.
   """

from blinker import signal
from mock import patch

from tutorial3 import app_crash, triage

@patch('tutorial3.error_report')
def test_has_receivers(error_report_mock):
    """The first app_crash does not call error_report because the signal
       has no receivers while the second app_crash does."""

    app_crash()
    error_report_mock.assert_not_called()

    signal('panic').connect(triage)
    app_crash()
    error_report_mock.assert_called_with()
