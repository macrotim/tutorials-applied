from flask.ext.testing import TestCase

from app import app

class MyTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_some_json(self):
        response = self.client.get("/ajax/")
        self.assertEquals(response.json['GoT'], 'Game of Thrones')

    def test_about(self):
        response = self.client.get("/about")
        self.assert_template_used("about.html")
