import os.path

from flask import Flask
from pre_request import pre

from application.BasicConfig import Config
from application.common.utils import response
from application.config import logging_config
from application.config.database import db
from application.config.json_config import JSONEncoderConfig
from application.config.pre_config import PreResponseConfig
from application.views import register


def create():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    app = Flask(path)

    # load config
    app.config.from_object(Config)

    # logging config
    logging_config.logging_handler(app)

    # json格式化
    app.json = JSONEncoderConfig(app)

    # pre_request config
    pre.add_response(PreResponseConfig)

    # init database
    db.init_app(app)

    # register application views
    register(app)

    app.json.ensure_ascii = False

    return app
