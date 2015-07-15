from flask import Flask
from flask_sqlite3.flask_sqlite3 import SQLite3

app = Flask(__name__)
db = SQLite3(app)

with app.app_context():
    cur = db.connection.cursor()
    print list(cur.execute("select date('now')"))
