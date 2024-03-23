from flask import Blueprint, current_app as current

from application.common.utils import response

route = Blueprint('demo_logging', __name__)


@route.route('/log', methods=['GET', 'POST'])
def log():
    current.logger.info('to fetch url %s', '/log')
    return response.success()
