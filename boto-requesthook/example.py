"""A simple demo of boto's Request Hook."""

import sys

from boto.s3.connection import S3Connection
from requestlog import RequestLogger

B = sys.argv[1]

conn = S3Connection()
conn.set_request_hook(RequestLogger())

# Read a file from S3.
print "Listing the contents of bucket", B
bucket = conn.get_bucket(B)
print list(bucket.list())
