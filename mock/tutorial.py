import mock

@mock.patch('__builtin__.open', autospec=True)
def test_open(mock_open):
    # Tim: I rewrote "with patch(...)" to @patch.
    handle = open('filename', 'r')
    mock_open.assert_called_with('filename', 'r')


def test_return():
    m = mock.Mock(return_value=3)
    assert m() == 3

    # Tim: Iterate through each return value.
    m = mock.Mock(side_effect=[4, 5, 6])
    assert m() == 4
    assert m() == 5
    assert m() == 6


def test_exception():
    # Tim: Force an exception.
    m = mock.Mock(side_effect=Exception('Boom!'))
    try:
        m()
        assert False
    except:
        assert True
