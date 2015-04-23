from flask.ext.testing import TestCase

from app import app, db
from model import User

class MyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite:///tmp/test.db"
    TESTING = True

    def create_app(self):
        return app

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

    def test_something(self):

        user = User()
        db.session.add(user)
        db.session.commit()
        assert user in db.session

        response = self.client.get("/about")
