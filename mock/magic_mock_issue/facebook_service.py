class FacebookService():
    def get_comment(self, comment_id):
        return Request().get('http://')

class Request():
    def get(self, url):
        raise NotImplementedError()
