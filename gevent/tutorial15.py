""" An extension of the Event object is the AsyncResult which allows you to send
    a value along with the wakeup call. This is sometimes called a future or a
    deferred, since it holds a reference to a future value that can be set on an
    arbitrary time schedule.
    """

import gevent
from gevent.event import AsyncResult
a = AsyncResult()

def setter():
    """
    After 3 seconds set the result of a.
    """
    gevent.sleep(3)
    a.set('Hello!')

def waiter():
    """
    After 3 seconds the get call will unblock after the setter
    puts a value into the AsyncResult.
    """
    print(a.get())

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
])
