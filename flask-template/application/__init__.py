import os.path

from flask import Flask

from application.views import register


def create():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    app = Flask(path)

    # register application views
    register(app)

    return app
