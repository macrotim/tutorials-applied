import json

from flask import Flask, render_template

from model import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route("/ajax/")
def some_json():
    return json.dumps({ 'GoT': 'Game of Thrones' })

@app.route("/about")
def about():
    return render_template("about.html")
