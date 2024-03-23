from flask import Blueprint
from pre_request import pre, Rule, ParamsValueError

from application.common.utils import response

route = Blueprint('precheck', __name__)

rule1 = {
    'name': Rule(required=True)
}


def required(value):
    if value is None or value == '':
        raise ParamsValueError('必填参数必填')
    return value


rule2 = {
    'name': Rule(required=True)
}


@route.post('/check/post')
@pre.catch(rule2)
def check_post():
    return response.success()
