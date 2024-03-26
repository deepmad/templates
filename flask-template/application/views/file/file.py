import os

from flask import Blueprint, request, current_app as current

from application.common.utils import parser, common, response, date, file, rand

route = Blueprint('file', __name__)


@route.post('/upload')
def upload():
    if parser.RequestParser.method() == 'GET':
        return response.failure('不支持此类型的方法')

    # 构造保存路径
    root = current.config.get('FILE_SAVE_ROOT')
    if common.is_empty(root):
        return response.failure('保存路径有误')

    files = request.files['file']
    _filename = files.filename

    # 截取文件后缀
    _subfix = file.subfix(_filename)
    if common.is_empty(_subfix):
        return response.failure('文件格式有误')

    # 创建路径
    path = "".join([root, os.sep, date.year_(), os.sep, date.month_(), os.sep, date.day_()])
    pathname = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + os.sep + path
    current.logger.info('pathname=%s', pathname)
    file.mkdir(pathname)
    filesize = files.content_length
    mimetype = files.mimetype

    # 保存文件
    key = rand.unique_()
    filename = "".join([key, '.', _subfix])
    files.save(os.path.join(pathname, filename))

    return response.success({
        'id': key,
        'filename': filename
    })


# @route.get('/image/preview')
# def preview(filename):
#    root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
#   return send_from_directory(root, filename)
