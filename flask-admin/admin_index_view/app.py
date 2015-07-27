"""Isolate AdminIndexView and practice with it.

"""
from flask import Flask, url_for, redirect, render_template, request
from flask.ext.admin import Admin, AdminIndexView


app = Flask(__name__)


class MyAdminIndexView(AdminIndexView):

    def _handle_view(self, name, **kwargs):

        if "tick" in request.args:
            return redirect(url_for("plaintext"))
        else:
            return super(MyAdminIndexView, self)._handle_view(name, **kwargs)


@app.route("/plaintext")
def plaintext():
    return "Just plain text here."


# Lesson: To override the admin index, "index_view" must be provided
#         when Admin is constructed.
admin = Admin(name='Example: AdminIndexView',
              index_view=MyAdminIndexView())

admin.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=5005)
