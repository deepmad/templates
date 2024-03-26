from typing import Any

from flask import request


class RequestParser:

    @classmethod
    def method(cls: Any) -> str:
        return request.method

    @classmethod
    def header(cls: Any, key):
        return request.headers.get(key)

    @classmethod
    def get(cls: Any, key, default=None):
        value = request.args.get(key, default=default, type=str)
        if value is None:
            value = request.form.get(key, default=default)
        if value is None:
            if request.is_json:
                value = request.get_json().get(key)
        return value

    @classmethod
    def all(cls):
        args = request.args
        forms = request.form
        jsons = {}
        if request.is_json:
            jsons = request.get_json()
        merge = {}
        for data in [args, forms, jsons]:
            merge.update(data)
        return merge

