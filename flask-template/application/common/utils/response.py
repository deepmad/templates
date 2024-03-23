import time

from flask import jsonify


def success(data=None, message='success', code=1):
    if data is None:
        return jsonify({
            'code': code,
            'message': message,
            'timestamp': int(time.time()*1000)
        })
    return jsonify({
        'code': code,
        'message': message,
        'data': data,
        'timestamp': int(time.time()*1000)
    })


def failure(message='error', code=0):
    return jsonify({
        'code': code,
        'message': message,
        'timestamp': int(time.time()*1000)
    })
