""" By default Responses will raise an assertion error if a url was registered
    but not accessed. This can be disabled by passing the
    assert_all_requests_are_fired value:
    """

import pytest
import responses
import requests

def test_okay():
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        rsps.add(responses.GET, 'http://twitter.com/api/1/foobar',
                 body='{}', status=200,
                 content_type='application/json')

def test_error():
    with pytest.raises(AssertionError):
        with responses.RequestsMock() as rsps: # assert_all_requests_are_fired omitted
            rsps.add(responses.GET, 'http://twitter.com/api/1/foobar',
                     body='{}', status=200,
                     content_type='application/json')
