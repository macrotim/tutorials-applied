from blinker import signal

# Subscribe to "ready" signal.

def subscriber(sender):
    print("Got a signal sent by %r" % sender)

ready = signal('ready')
ready.connect(subscriber)

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

processor_a = Processor('a')
processor_a.go()

# Sending and Receiving Data Through Signals

send_data = signal('send-data')

@send_data.connect
def receive_data(sender, **kw):
    print("Caught signal from %r, data %r" % (sender, kw))
    return 'received!'

result = send_data.send('anonymous', abc=123)
print result

# Optimizing Signal Sending

def error_report():
    print "free(): Imagine this is an expensive method to call... we want to minimize calls."

def app_crash():
    panic = signal('panic')
    if panic.receivers: # skip if no subscribers
        panic.send("app_crash", error_report=error_report())

def triage(sender, **kw):
    print "Triage an error report"

app_crash() # should not send the panic signal
signal('panic').connect(triage)
app_crash()
