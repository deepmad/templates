from flask import Blueprint
from sqlalchemy import text

from application.common.utils import response, common
from application.config.database import db
from application.models.system.sys_user import SysUser

route = Blueprint('auth', __name__)


@route.route('/token')
def token():
    SysUser.query.all()
    users = db.session.execute(db.select(SysUser)).scalars().all()
    rows = db.session.execute(text('select * from dm_sys_user'))
    return response.success(common.cursor2list(rows))
