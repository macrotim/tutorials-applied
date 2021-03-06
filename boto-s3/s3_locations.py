"""To put the boto.s3 API into practice, lets benchmark reading and writing to
   buckets located around the world."""

import random
import time
import string
import sys
import textwrap

import boto
from boto.s3.connection import S3Connection
from boto.s3.connection import Location
from boto.s3.key import Key

LOCATIONS = (Location.SAEast, Location.USWest2, Location.USWest, Location.EU)

def run_benchmark(bucket_prefix, locations, num_files=10):
    """Run a benchmark against S3 buckets in different locations."""

    conn = S3Connection()
    for location in locations:
        print
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
        n = num_files

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


if __name__ == "__main__":
    if len(sys.argv) > 1:
        bucket_prefix = sys.argv[1]
    else:
        print """USAGE: ./script <bucket-prefix>"""
        print textwrap.dedent("""
            Whatever bucket-prefix you choose, four new buckets
            will be created, one for each location:
            %s""" % ", ".join(LOCATIONS))
        sys.exit()

    run_benchmark(bucket_prefix, LOCATIONS)
