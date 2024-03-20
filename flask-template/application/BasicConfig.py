from urllib.parse import quote_plus as urlquote


class Config:
    MYSQL_USERNAME = 'deepmad'
    MYSQL_PASSWORD = 'deepmad'
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_DATABASE = 'templates'
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USERNAME}:{urlquote(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4'
