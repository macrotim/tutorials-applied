"""In a more common use case, asynchronously fetching data from a server, the
   runtime of fetch() will differ between requests, depending on the load on
   the remote server at the time of the request.

   Tim: I changed the URL because it was throwing a 404.
   """

import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import simplejson as json

def fetch(pid):
    response = urllib2.urlopen('http://httpbin.org/get')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['origin']

    print('Process %s: %s' % (pid, datetime))
    return json_result['origin']

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
