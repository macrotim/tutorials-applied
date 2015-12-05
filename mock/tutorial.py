"""Light exercises with the mock module."""

from mock import patch, Mock
import pytest

def test_open1():
    with patch('__builtin__.open', autospec=True) as mock_open:
        handle = open('robots.txt', 'r')
        mock_open.assert_called_with('robots.txt', 'r')

# Tim: Functionally equivalent to test_open1.
@patch('__builtin__.open', autospec=True)
def test_open2(mock_open):
    handle = open('robots.txt', 'r')
    mock_open.assert_called_with('robots.txt', 'r')

def test_return():
    # Tim: Return a stubbed value.
    m = Mock(return_value=3)
    assert m() == 3

    # Tim: Return a list.
    m = Mock(return_value=[4, 5, 6])
    assert m() == [4, 5, 6]

    # Tim: Return a different value for each call.
    m = Mock(side_effect=[4, 5, 6])
    assert m() == 4
    assert m() == 5
    assert m() == 6
    pytest.raises(StopIteration, m)

def test_exception():
    # Tim: Force an exception.
    m = Mock(side_effect=Exception('Boom!'))
    pytest.raises(Exception, m)

def test_sideeffect():
    # Tim: Mock.side_effect takes a lambda.
    m = Mock()
    m.side_effect = lambda x: {42: "Called with 42", 43: "Called with 43"}.get(x)
    assert m(42) == "Called with 42"
    assert m(43) == "Called with 43"

    # Tim: Alternatively, pass a function.
    def my_side_effect(*args, **kwargs):
        return {
            42: "Called with 42",
            43: "Called with 43"
        }.get(args[0])
    m = Mock()
    m.side_effect = my_side_effect
    assert m(42) == "Called with 42"
    assert m(43) == "Called with 43"


