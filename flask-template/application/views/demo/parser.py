from flask import Blueprint

from application.common.utils import response, parser

route = Blueprint('demo_parser', __name__)


@route.route('/params', methods=['GET', 'POST'])
def params():
    value = parser.RequestParser.get(key="key")
    return response.success(data={
        'key': value
    })
