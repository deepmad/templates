from flask import Response

from application import create
from application.common.utils import response, parser

app = create()


@app.before_request
def before_request():
    params = parser.RequestParser.all()
    app.logger.info('request params=%s', params)


#@app.after_request
def after_request(resp: Response):
    if resp.is_json:
        app.logger.info('request response=%s', resp.get_json())
    else:
        app.logger.info('request response is not json')
    return resp


@app.errorhandler(500)
def interval_error_handler(error):
    app.logger.error('interval_error_handler error=%s', error)
    return response.failure(message='系统发生异常')


@app.errorhandler(404)
def notfound_error_handler(error):
    app.logger.error('notfound_error_handler error=%s', error)
    return response.failure(message='暂无访问权限')


@app.errorhandler(405)
def not_allowed_error_handler(error):
    app.logger.error('not_allowed_error_handler error=%s', error)
    return response.failure(message='暂无访问权限')


@app.errorhandler(Exception)
def teardown_request(error):
    app.logger.error('common_error_handler error=%s', error)
    return response.failure(message='请求发生异常，请稍后再试')


if __name__ == '__main__':
    app.run()
