import datetime

from flask import Blueprint
from sqlalchemy import text

from application import db
from application.common.utils import response, common
from application.models.system.sys_user import SysUser

route = Blueprint('demo', __name__)


@route.route('/select/model')
def select_model():
    SysUser.query.all()
    result = db.session.execute(db.select(SysUser)).scalars().all()
    return response.success(common.models2list(result))


@route.route('/select/native')
def select_native():
    rows = db.session.execute(text('select * from dm_sys_user'))
    return response.success(common.cursor2list(rows))


@route.route('/add/model')
def add_model():
    user = SysUser(id=1, account='account', create_dt=datetime.datetime.now())
    db.session.add(user)
    db.session.commit()
    return response.success()


@route.route('/delete/model')
def delete_model():
    user = SysUser.query.filter(SysUser.id == 1).first()
    db.session.delete(user)
    db.session.commit()
    return response.success()


@route.route('/update/model')
def update_model():
    users = SysUser.query.filter(SysUser.flag == 1)
    for user in users:
        user.create_dt = datetime.datetime.now()
    db.session.commit()
    return response.success()