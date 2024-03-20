import datetime
import json

from application.config.database import db


class SysUser(db.Model):
    __tablename__ = 'dm_sys_user'

    id = db.Column(db.BIGINT, primary_key=True, comment='主键id')
    account = db.Column(db.String(50), comment='账号')
    name = db.Column(db.String(50), comment='名称')
    phone = db.Column(db.String(20), comment='手机')
    password = db.Column(db.String(100), comment='密码')
    salt = db.Column(db.String(100), comment='盐值')
    flag = db.Column(db.INT, comment='状态标识（0-无效；1-有效）')
    create_dt = db.Column('create_dt', db.DateTime, default=datetime.datetime.now(), comment='创建时间')

    def to_json(self):
        return json.dumps({
            'id': self.id,
            'account': self.account,
            'name': self.name,
            'phone': self.phone,
            'password': self.password,
            'salt': self.salt,
            'flag': self.flag,
            'create_dt': self.create_dt
        })
