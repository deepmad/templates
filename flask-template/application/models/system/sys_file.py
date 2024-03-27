import datetime

from application import db
from application.common.utils import common


class SysFile(db.Model):
    __tablename__ = 'dm_sys_file'

    id = db.Column(db.BIGINT, primary_key=True, comment='主键id')
    origin_file_name = db.Column(db.String(200), comment='文件原始名称')
    file_name = db.Column(db.String(200), comment='文件名称')
    file_path = db.Column(db.String(200), comment='文件路径')
    file_size = db.Column(db.INT, comment='文件大小')
    file_subfix = db.Column(db.String(50), comment='文件后缀')
    mimetype = db.Column(db.String(50), comment='文件类型')
    create_dt = db.Column('create_dt', db.DateTime, default=datetime.datetime.now(), comment='创建时间')

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def select(cls, key):
        cls.query.filter(cls.id == key)
        result = db.session.execute(db.select(cls)).scalars().all()
        return common.models2list(result)
