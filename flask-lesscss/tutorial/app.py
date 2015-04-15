from flask import Flask, render_template

app = Flask(__name__)

# Beware that flask-lesscss errors out when app.static_path is undefined.
# It also errors out if the dir name is missing the "/" character.
# Unfortunately, this is not documented.
app.static_path = '/static'

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    from flaskext.lesscss import lesscss
    lesscss(app)
    app.run(debug=True)
