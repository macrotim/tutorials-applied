"""Send tasks to the Celery daemon."""

import sys
import time
from tasks import crawl

if len(sys.argv) < 2:
    print """Usage: task_writer.py <seconds>"""
    sys.exit(-1)
else:
    wait = int(sys.argv[1])

while True:
    crawl.delay('http://flower.readthedocs.org')
    time.sleep(wait)
