from typing import Any

from sqlalchemy import Result


def model2dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}


def models2list(obj):
    return [model2dict(c) for c in obj]


def cursor2list(rows: Result):
    return [dict(row) for row in rows.mappings()]


def is_empty(obj: Any) -> bool:
    if obj is None:
        return True
    if isinstance(obj, str):
        if obj == '' or len(obj) == 0:
            return True
    if isinstance(obj, dict) or isinstance(obj, list) or isinstance(obj, tuple):
        if not obj or len(obj) == 0:
            return True
    return False

