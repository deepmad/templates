from flask import jsonify


def success(data=None, message='success', code=1):
    if data is None:
        return jsonify({
            'code': code,
            'message': message
        })
    return jsonify({
        'code': code,
        'message': message,
        'data': data
    })


def failure(message='error', code=0):
    return jsonify({
        'code': code,
        'message': message
    })
