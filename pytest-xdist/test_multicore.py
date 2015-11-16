"""A simple demo that distributes tests across multiple cores.

   Run the test with:
       py.test -n auto test_multicore.py
   """

import time

def test_sleep1():
    time.sleep(1)

def test_sleep2():
    time.sleep(1)

def test_sleep3():
    time.sleep(1)

def test_sleep4():
    time.sleep(1)

def test_sleep5():
    time.sleep(1)

def test_sleep6():
    time.sleep(1)
