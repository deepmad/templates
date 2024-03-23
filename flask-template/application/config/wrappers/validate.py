import datetime
from functools import wraps

from application.BasicError import BasicError
from application.common.utils import parser, common
from application.config.jwt_config import JwtToken


def validation(codes: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'token' in codes:
                token = parser.RequestParser.header('Authorization')
                if common.is_empty(token):
                    raise BasicError('token不能为空')
                token = token[7:]
                try:
                    _payload = JwtToken.parse(token)
                    _expire: int = _payload.get('exp')
                    if _expire is not None:
                        # 比对时间是否过期
                        now = int(datetime.datetime.now().timestamp())
                        if now > _expire:
                            raise BasicError('token有效期过期')
                except Exception as error:
                    raise BasicError('token有效期过期')
            return func(*args, **kwargs)

        return wrapper

    return decorator
