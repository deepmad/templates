from flask import jsonify, Blueprint

from application.common.utils import response

route = Blueprint('auth', __name__)


@route.route('/token')
def token():
    return response.success()
