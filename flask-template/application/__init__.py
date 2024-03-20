import os.path

from flask import Flask

from application.BasicConfig import Config
from application.config.database import db
from application.config.json_config import JSONEncoderConfig
from application.views import register


def create():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    app = Flask(path)

    # load config
    app.config.from_object(Config)

    # json格式化
    app.json = JSONEncoderConfig(app)

    # init database
    db.init_app(app)

    # register application views
    register(app)

    return app
