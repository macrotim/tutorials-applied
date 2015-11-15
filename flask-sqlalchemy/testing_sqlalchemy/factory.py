from flask import Flask

def create_app(name, settings_override):
    app = Flask(__name__)
    app.config.from_object(settings_override)
    return app
