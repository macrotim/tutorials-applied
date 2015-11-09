"""Blinker tutorial: Sending and Receiving Data Through Signals"""

from blinker import signal

send_data = signal('send-data')

@send_data.connect
def receive_data_wrapper(sender, **kw):
    """The wrapper allows the method to be unit tested."""
    receive_data(sender, **kw)

def receive_data(sender, **kw):
    print("Caught signal from %r, data %r" % (sender, kw))
    return 'received!'

if __name__ == '__main__':
    result = send_data.send('anonymous', abc=123)
    print result
