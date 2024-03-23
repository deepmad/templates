from flask import Flask

from application.views.auth.auth import route as views_auth_auth
from application.views.demo.db import route as views_demo_db
from application.views.demo.parser import route as views_demo_parser
from application.views.demo.precheck import route as views_demo_precheck


def register(app: Flask):
    app.register_blueprint(views_auth_auth, url_prefix='/auth')
    app.register_blueprint(views_demo_db, url_prefix='/demo/db')
    app.register_blueprint(views_demo_parser, url_prefix='/demo/parser')
    app.register_blueprint(views_demo_precheck, url_prefix='/demo/pre_check')
