"""A response can also throw an exception as follows."""

import responses
import requests
from requests.exceptions import HTTPError

exception = HTTPError('Something went wrong')
responses.add(responses.GET, 'http://twitter.com/api/1/foobar',
              body=exception)
# All calls to 'http://twitter.com/api/1/foobar' will throw exception.
