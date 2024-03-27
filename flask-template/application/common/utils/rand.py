import datetime
import random
import string
import uuid


def string_(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def uuid_():
    return str(uuid.uuid4()).replace('-', '')


def digits_(length):
    letters = string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def unique_():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + digits_(4)


def key_():
    return datetime.datetime.now().strftime('%y%m%d%H%M%S%f')[:-2] + digits_(3)
