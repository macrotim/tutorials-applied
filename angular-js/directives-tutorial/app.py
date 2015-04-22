from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/<path:filename>')
def base_static(filename):
    return send_from_directory(app.root_path, filename)

app.run(debug=True)
