from flask import Flask, flash, render_template, redirect, request, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from model import db, User

app = Flask(__name__)
app.secret_key = 'a super secret key'

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated():
        return redirect("/profile")

    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form.get('email').strip()
        user = validate_login(email)
        if user:
            login_user(user)
            flash("Logged in successfully.")
            return redirect("/profile")
        else:
            flash("No account exists for {}".format(email))
            return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/login")

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")

def validate_login(email):
    """User authentication for this tutorial is rudimentary."""
    if email:
        users = User.query.filter(User.email == email).all()
        if len(users) == 1:
            return users[0]
    return None

def refresh_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add(User(username='bill.murray', email='bill@groundhogday.com'))
        db.session.commit()

if __name__ == '__main__':
    refresh_db()
    app.run(debug=True)
