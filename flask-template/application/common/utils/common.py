from sqlalchemy import CursorResult, Result


def model2dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}


def models2list(obj):
    return [model2dict(c) for c in obj]


def cursor2list(rows: Result):
    return [dict(row) for row in rows.mappings()]
