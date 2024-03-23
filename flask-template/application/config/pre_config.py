import json
import typing as t

from flask import Response
from pre_request import ParamsValueError
from pre_request.response import JSONResponse


class PreResponseConfig(JSONResponse):

    @classmethod
    def make_response(
            cls,
            error: ParamsValueError,
            fuzzy: bool = False,
            formatter: t.Optional[t.Callable] = None
    ) -> Response:
        result = {
            'code': -1,
            'message': error.message
        }

        # use formatter function to handler error message
        if formatter and error:
            result = formatter(error)

        from flask import make_response  # pylint: disable=import-outside-toplevel
        response = make_response(json.dumps(result, ensure_ascii=False))
        response.headers["Content-Type"] = "application/json; charset=utf-8"

        return response
