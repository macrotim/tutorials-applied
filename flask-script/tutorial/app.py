from flask import Flask

from model import User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

def refresh_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add(User(username='bill.murray', email='bill@groundhogday.com'))
        db.session.commit()

print "Refreshing database..."
refresh_db()
