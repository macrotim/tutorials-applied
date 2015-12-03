"""Use tmpdir_factory to create tmp directories and files only once."""

import pytest

@pytest.fixture(scope='session')
def image_file(tmpdir_factory):
    img = '0' * 2**20
    fn = tmpdir_factory.mktemp('data').join('img.txt')
    fn.write(img)
    return fn

def test_histogram(image_file):
    img = image_file.read()
    assert len(img) == 2**20
