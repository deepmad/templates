from flask import Blueprint
from pre_request import Rule, pre

from application.common.utils import response, parser
from application.config.jwt_config import JwtToken
from application.config.rules import rule

route = Blueprint('auth', __name__)

rule1 = {
    'account': Rule(required=True, callback=rule.required)
}


@route.post('/token')
@pre.catch(rule1)
def token():
    account = parser.RequestParser.get('account')
    _payload = {
        'account': account
    }
    _token = JwtToken.generate(_payload, expire=10)
    return response.success({
        'token': _token
    })
