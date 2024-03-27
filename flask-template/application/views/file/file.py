import datetime
import os

from flask import Blueprint, request, current_app as current, send_from_directory

from application.BasicError import BasicError
from application.common.utils import parser, common, response, date, file, rand
from application.models.system.sys_file import SysFile

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
    path = "".join([date.year_(), os.sep, date.month_(), os.sep, date.day_()])
    pathname = os.path.abspath("".join([root, os.sep, path]))
    current.logger.info('pathname=%s', pathname)
    file.mkdir(pathname)
    filesize = files.content_length
    mimetype = files.mimetype

    # 保存文件
    filename = "".join([rand.unique_(), '.', _subfix])
    files.save(os.path.join(pathname, filename))

    file_id = rand.key_()
    SysFile.save(SysFile(
        id=file_id,
        origin_file_name=_filename,
        file_name=filename,
        file_path="".join([path, os.sep, filename]),
        file_size=0,
        file_subfix=_subfix,
        mimetype=mimetype,
        create_dt=datetime.datetime.now()
    ))

    return response.success({
        'id': file_id,
        'filename': filename
    })


@route.get('/image/preview')
def preview():
    key = parser.RequestParser.get('id')
    files = SysFile.select(key)
    if common.is_empty(files):
        raise BasicError('访问数据异常')

    root = current.config.get('FILE_SAVE_ROOT')
    if common.is_empty(root):
        raise BasicError('保存路径有误')

    root = os.path.abspath(root)
    return send_from_directory(root, files[0].get('file_path'))
