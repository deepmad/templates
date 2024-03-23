from flask import Blueprint

from application.common.utils import response
from application.config.wrappers.validate import validation

route = Blueprint('demo_validation', __name__)


@route.post('/validation')
@validation(codes=['token'])
def validation():
    return response.success()
