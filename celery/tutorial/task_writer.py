"""Send tasks to the Celery daemon."""

import time
from tasks import add

# Add a task to Celery.
# "result" requires that the Celery's result-backend is enabled.
result = add.delay(4, 4)
while not result.ready():
    time.sleep(.1)
print 'Ready?', result.ready()
print 'Result:', result.get() # Makes the async call synchronous!
print

# Create a task that errors out.
result = add.delay(4, '')
while not result.ready():
    time.sleep(.1)
print 'Ready?', result.ready()
print 'Result:', result.get(propagate=False)
print 'Stacktrace:', result.traceback
