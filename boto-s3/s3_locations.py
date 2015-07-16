"""Benchmark time to put and get from buckets in various locations."""

import random
import time
import string
import sys

import boto
from boto.s3.connection import S3Connection
from boto.s3.connection import Location
from boto.s3.key import Key

bucket_prefix = sys.argv[1]
conn = S3Connection()

for location in (Location.SAEast, Location.USWest2, Location.USWest, Location.EU):
    print "> Benchmarking against", location

    # Create or get the bucket.
    bucket_name = (bucket_prefix + "-" + location).lower()
    try:
        bucket = conn.create_bucket(bucket_name, location=location)
    except boto.exception.S3CreateError:
        print "Bucket exists. Deleting it."
        bucket = conn.get_bucket(bucket_name)
        for key in bucket.list():
            key.delete()
        bucket = conn.delete_bucket(bucket_name)
        bucket = conn.create_bucket(bucket_name, location=location)

    start = time.time()
    n = 10

    # Put N random files in the bucket.
    print "Putting {} files.".format(n)
    for file_count in xrange(n):
        key = Key(bucket)
        key.key = '1024kb.' + str(file_count)
        key.set_contents_from_string(''.join([random.choice(string.ascii_letters + string.digits) for _ in xrange(1024)]))

    # Get each file.
    print "Getting each file."
    file_counts = range(n)
    random.shuffle(file_counts)
    for file_count in file_counts:
        key = Key(bucket)
        key.key = '1024kb.' + str(file_count)
        key.get_contents_as_string()

    print 'Elapsed:', time.time() - start, 'sec'
