Testing Flask Apps
==================

Flask provides a way to test your application by exposing the Werkzeug test Client and handling the context locals for you. You can then use that with your favourite testing solution. In this documentation we will use the unittest package that comes pre-installed with Python.

`Overview`_.

Unit testing looks cleaner in an unstable build of Flask-1.0. Try it out: 

  cd flaskr-0.10.1
  py.test flaskr_tests_new.py

.. _Overview: http://flask.pocoo.org/docs/0.10/testing/

Flask-Testing
=============

The Flask-Testing extension provides unit testing utilities for Flask.

`Overview`_.

.. _Overview: https://pythonhosted.org/Flask-Testing/
