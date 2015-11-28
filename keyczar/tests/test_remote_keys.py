"""This is an exercise to unit test code that performs IO."""

import os
import shutil
from mock import patch, MagicMock
from remote_keys import demo

DIR = os.path.dirname(os.path.abspath(__file__))
TESTKEY = os.path.join(DIR, 'keyczar-testkey.tgz')

@patch('remote_keys.urllib.urlretrieve')
def test_demo(mock_urlretrieve):
    def copy(url, to):
        shutil.copyfile(TESTKEY, to)
    mock_urlretrieve.side_effect = copy

    test_string = 'test_string'
    encrypted, decrypted = demo(test_string)
    assert test_string == decrypted
