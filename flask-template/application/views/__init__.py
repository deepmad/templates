from flask import Flask
from application.views.auth.auth import route as views_auth_auth
from application.views.demo.db import route as views_demo_db


def register(app: Flask):
    app.register_blueprint(views_auth_auth, url_prefix='/auth')
    app.register_blueprint(views_demo_db, url_prefix='/demo/db')
