""" Greenlets that fail to yield when the main program receives a SIGQUIT may
    hold the program's execution longer than expected. This results in so called
    "zombie processes" which need to be killed from outside of the Python
    interpreter.

    A common pattern is to listen SIGQUIT events on the main program and to
    invoke gevent.shutdown before exit.
    """

import gevent
import signal

def run_forever():
    gevent.sleep(1000)

if __name__ == '__main__':
    gevent.signal(signal.SIGQUIT, gevent.kill)
    thread = gevent.spawn(run_forever)
    thread.join()
