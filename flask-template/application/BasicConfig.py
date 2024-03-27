import logging
from urllib.parse import quote_plus as urlquote


class Config:
    # file config
    FILE_SAVE_ROOT = '/datas'

    # jwt config
    JWT_SECRET = ''

    # logging
    LOG_LEVEL = logging.DEBUG
    LOG_PATH = '../log'
    LOG_PREFIX = 'daily'
    LOG_MAX = 1024*1024

    MYSQL_USERNAME = 'deepmad'
    MYSQL_PASSWORD = 'deepmad'
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_DATABASE = 'templates'
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USERNAME}:{urlquote(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4'
