import json
from typing import Any

from flask import request


class RequestParser:
    @classmethod
    def header(cls: Any, key):
        return request.headers.get(key)

    @classmethod
    def get(cls: Any, key, default=None):
        value = request.args.get(key, default=default)
        if value is None:
            value = request.form.get(key, default=default)
        if value is None:
            value = request.get_json().get(key)
        return value
