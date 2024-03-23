import datetime
import time

import jwt
from flask import current_app as current

from application.common.utils import rand


class JwtToken:

    @classmethod
    def generate(cls, payload, expire=-1):
        _secret = current.config['JWT_SECRET']
        _iat = int(datetime.datetime.now().timestamp())
        _timestamp = int(time.time() * 1000)
        _random = rand.string_(16)
        _payload = {
            'iss': '4Rjq@iar$hRt%a^e0kkMyGY*TNu$a0#',
            'iat': _iat,
            'timestamp': int(time.time() * 1000),
            'random': _random
        }
        if expire != -1:
            _payload.update({
                'exp': _iat + expire
            })
        _payload.update(payload)
        _token = jwt.encode(_payload, _secret, algorithm='HS256')
        token = {
            'token': _token,
            'random': _random,
            'timestamp': _timestamp
        }
        if expire != -1:
            token.update({
                'exp': _iat + expire
            })
        return token

    @classmethod
    def parse(cls, token) -> dict:
        _secret = current.config['JWT_SECRET']
        try:
            _payload = jwt.decode(token, _secret, algorithms=['HS256'])
        except Exception as error:
            current.logger.error('jwt parse error=%s', error)
            raise error
        return _payload
