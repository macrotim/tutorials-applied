import mock

class FacebookService(object):

    num_posts = 0

    def post_comment(self, message):
        self.internal(1, 2, 3, message)

    def internal(self, a, b, c, message):
        print "Invoked FacebookService.internal"


@mock.patch.object(FacebookService, "internal", autospec=True)
def test1(mock_internal):
    m = "real men write unit tests"
    real = FacebookService()
    real.post_comment(message=m)
    mock_internal.assert_called_once_with(real, 1, 2, 3, m)


@mock.patch.object(FacebookService, "num_posts", mock.sentinel.attribute)
def test2():
    assert FacebookService.num_posts == mock.sentinel.attribute



