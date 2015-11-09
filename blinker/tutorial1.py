"""Blinker tutorial: Subscribe to "ready" signal."""

from blinker import signal

def subscriber(sender):
    print("Got a signal sent by %r" % sender)

def subscriber_wrapper(sender):
    """The wrapper is necessary to allow for unit testing."""
    subscriber(sender)

ready = signal('ready')
ready.connect(subscriber_wrapper)

# Emit the "ready" signal.

class Processor:
    def __init__(self, name):
        self.name = name

    def go(self):
        ready = signal('ready')
        ready.send(self)
        print("Processing.")
        complete = signal('complete')
        complete.send(self)

    def __repr__(self):
        return '<Processor %s>' % self.name

if __name__ == '__main__':
    processor_a = Processor('a')
    processor_a.go()
