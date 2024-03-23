import logging
import os
import time
from logging.handlers import RotatingFileHandler

from flask import Flask

from application.common.utils import file


def logging_handler(app: Flask):
    config = app.config
    path = config.get('LOG_PATH')
    prefix = config.get('LOG_PREFIX')
    log_max = config.get('LOG_MAX')

    filename = (prefix if prefix is not None else 'daily') + '-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    pathname = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + os.sep + path
    file.mkdir(pathname)
    logging.basicConfig(level=config.get('LOG_LEVEL'))
    handler = RotatingFileHandler(pathname + os.sep + filename, maxBytes=log_max, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

