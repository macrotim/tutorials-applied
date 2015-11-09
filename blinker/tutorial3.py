"""Blinker Tutorial: Optimizing Signal Sending"""

from blinker import signal

def error_report():
    print "free(): Imagine this is an expensive method to call... we want to minimize calls."

def app_crash():
    panic = signal('panic')
    if panic.receivers: # skip if no subscribers
        panic.send("app_crash", error_report=error_report())

def triage(sender, **kw):
    print "Triage an error report"


if __name__ == '__main__':
    app_crash() # should not send the panic signal
    signal('panic').connect(triage)
    app_crash()
