from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)
app.config['ASSETS_DEBUG'] = False

js = Bundle('js/jquery.min.js', 'js/hello.js',
            filters='jsmin', output='gen/packed.js')
assets.register('js_all', js)

@app.route("/test1")
def test1():
    return render_template("test1.html")

@app.route("/test2")
def test2():
    return render_template("test2.html")

app.run(debug=True)
