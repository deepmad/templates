from flask import Flask
from application.views.auth.auth import route as views_auth_auth


def register(app: Flask):
    app.register_blueprint(views_auth_auth, url_prefix='/auth')
