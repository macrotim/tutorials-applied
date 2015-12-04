gevent
======

gevent is a concurrency library based around libev. It provides a clean API for a variety of concurrency and network related tasks.

`Tutorial`_

.. _Tutorial: http://sdiehl.github.io/gevent-tutorial/

OSX Installation
================

There are a few hurdles to install gevent on OSX. Here's what I did.

    brew install libevent

Assuming that libevent was installed at /usr/local/Cellar/libevent/2.0.22:

    export CFLAGS="-I /usr/local/Cellar/libevent/2.0.22/include -L /usr/local/Cellar/libevent/2.0.22/lib"
    CFLAGS='-std=c99' pip install gevent
