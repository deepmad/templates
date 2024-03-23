from pre_request import ParamsValueError

from application.common.utils import common


def required(value):
    if common.is_empty(value):
        raise ParamsValueError('必填参数不能为空')
    return value
