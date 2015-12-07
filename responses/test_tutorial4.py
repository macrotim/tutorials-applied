""" Instead of passing a string URL into responses.add or responses.add_callback
    you can also supply a compiled regular expression.

    Tim: This example only does configuration and does not perform any actions.
    """

import re
import responses
import requests

# Instead of
responses.add(responses.GET, 'http://twitter.com/api/1/foobar',
              body='{"error": "not found"}', status=404,
              content_type='application/json')

# You can do the following
url_re = re.compile(r'https?://twitter.com/api/\d+/foobar')
responses.add(responses.GET, url_re,
              body='{"error": "not found"}', status=404,
              content_type='application/json')
