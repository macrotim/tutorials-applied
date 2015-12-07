"""Responses as a context manager"""

import responses
import requests

def test_my_api():
    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, 'http://twitter.com/api/1/foobar',
                 body='{}', status=200,
                 content_type='application/json')
        resp = requests.get('http://twitter.com/api/1/foobar')

        assert resp.status_code == 200

    # outside the context manager requests will hit the remote server
    resp = requests.get('http://twitter.com/api/1/foobar')
    resp.status_code == 404
