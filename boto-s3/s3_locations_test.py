"""In this exercise, I include unit tests for the boto.s3 benchmark."""

import unittest

from boto.exception import S3CreateError
from boto.s3.connection import Location
from mock import patch

from s3_locations import run_benchmark

class RunBenchmarkTest(unittest.TestCase):

    @patch('s3_locations.S3Connection.create_bucket')
    def test_create_bucket(self, create_bucket_mock):
        run_benchmark('boto-benchmark-unit-test', (Location.USWest,), num_files=0)
        create_bucket_mock.assert_called_with('boto-benchmark-unit-test-us-west-1', location=Location.USWest)

    @patch('s3_locations.S3Connection.delete_bucket')
    @patch('s3_locations.S3Connection.get_bucket')
    @patch('s3_locations.S3Connection.create_bucket')
    def test_get_bucket(self, create_bucket_mock, get_bucket_mock, delete_bucket_mock):
        create_bucket_mock.side_effect = (
            S3CreateError(1, 2, 3), # Error the first time.
            None)                   # Do nothing the second time.

        run_benchmark('boto-benchmark-unit-test', (Location.USWest,), num_files=0)

        b = 'boto-benchmark-unit-test-us-west-1'
        get_bucket_mock.assert_called_with(b)
        delete_bucket_mock.assert_called_with(b)
        create_bucket_mock.assert_called_with(b, location=Location.USWest)
