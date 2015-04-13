import os

from flask import Flask, request
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView

import model

app = Flask(__name__)
app.secret_key = 'super secret key'

# Configure SQLAlchemy.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
model.db.init_app(app)
model.db.create_all(app=app)

# Set the header to "Awesome Admin".
admin = Admin(app, name="Awesome Admin")

# Define a simple admin page.
class MyView1(BaseView):
    def is_accessible(self):
        # Enable or disable this view by appending ?hello the URL.
        return 'hello' in request.args

    @expose('/')
    def index(self):
        return self.render('index.html')

# Define another admin page.
class MyView2(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')

# Add "Hello" to the menu which refers to the URL /admin/myview1.
admin.add_view(MyView1(name='Hello'))

# Add a dropdown "Test" to the menu. Each item refers to /admin/{endpoint}.
admin.add_view(MyView2(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(MyView2(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(MyView2(name='Hello 3', endpoint='test3', category='Test'))

# Create an admin page for the User model.
admin.add_view(ModelView(model.User, model.db.session))

# Create a custom admin page for the Product model.
class ProductView(ModelView):
    can_create = True

    # Override displayed fields
    column_list = ('title',)

    def __init__(self, **kwargs):
        # You can pass name and other parameters if you want to
        super(ProductView, self) \
            .__init__(model.Product, model.db.session, **kwargs)

admin.add_view(ProductView())

if __name__ == '__main__':
    app.run(debug=True)
