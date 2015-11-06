"""In this exercise, I include unit tests for the boto.s3 benchmark.
   Instead of building functional tests that exercise against S3, I use
   the mock module to stop network requests. This has the benefit of
   isolating the unit under test and avoids a choke point that would
   slow unit tests to a crawl.

   Use py.test to run the test.
   """

import unittest

from boto.exception import S3CreateError
from boto.s3.connection import Location
from mock import patch

from s3_locations import run_benchmark

class PatcherStartStopTest(unittest.TestCase):

    def setUp(self):
        patcher = patch('s3_locations.S3Connection')
        self.s3_connection_mock = patcher.start()
        self.s3_connection_mock.return_value = self.s3_connection_mock
        self.addCleanup(patcher.stop)

    def test_pass(self):
        run_benchmark('boto-benchmark-unit-test', [], num_files=0)
        self.s3_connection_mock.assert_not_called()

    def test_create_bucket(self):
        run_benchmark('boto-benchmark-unit-test', (Location.USWest,), num_files=0)
        self.s3_connection_mock.create_bucket.assert_called_with('boto-benchmark-unit-test-us-west-1', location=Location.USWest)

    def test_get_bucket(self):
        self.s3_connection_mock.create_bucket.side_effect = (
            S3CreateError(1, 2, 3), # Error the first time.
            None)                   # Do nothing the second time.

        run_benchmark('boto-benchmark-unit-test', (Location.USWest,), num_files=0)

        b = 'boto-benchmark-unit-test-us-west-1'
        self.s3_connection_mock.get_bucket.assert_called_with(b)
        self.s3_connection_mock.delete_bucket.assert_called_with(b)
        self.s3_connection_mock.create_bucket.assert_called_with(b, location=Location.USWest)
