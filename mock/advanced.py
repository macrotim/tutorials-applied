from mock import patch
import pytest


def test_date():
    from datetime import date
    import foobar
    with patch('foobar.date') as mock_date:
        # Patch date.today.
        mock_date.today.return_value = date(2010, 10, 8)

        # Patch date (the constructor).
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

        assert foobar.date.today() == date(2010, 10, 8)
        assert foobar.date(2009, 6, 8) == date(2009, 6, 8)


@pytest.fixture()
def mocks(request):
    patcher = patch('foobar.foo', autospec=True)
    mock_foo = patcher.start()
    request.addfinalizer(lambda: patcher.stop())
    return mock_foo,


def test_setup_teardown(mocks):
    # The mocks are setup via the "mocks" fixture.
    mock_foo, = mocks
    mock_foo()
    mock_foo.assert_called_with()
