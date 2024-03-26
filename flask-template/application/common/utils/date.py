from datetime import datetime

from application.common.utils import common


def fmt_(time: datetime = None, fmt: str = None):
    if time is None:
        time = datetime.now()
    if common.is_empty(fmt):
        fmt = '%Y-%m-%d %H:%M:%S'
    return time.strftime(fmt)


def year_(time: datetime = None, fmt: str = None):
    return fmt_(fmt='%Y')


def month_(time: datetime = None, fmt: str = None):
    return fmt_(fmt='%m')


def day_(time: datetime = None, fmt: str = None):
    return fmt_(fmt='%d')
