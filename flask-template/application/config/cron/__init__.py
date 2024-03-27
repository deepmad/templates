from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_apscheduler import APScheduler

scheduler = APScheduler(BackgroundScheduler(timezone='Asia/Shanghai', api_enabled=True))


# https://blog.csdn.net/m0_38039437/article/details/130196860

def register(app: Flask):
    scheduler.init_app(app)
    scheduler.start()


def _cron(expression):
    args = {}
    expressions = expression.split(' ')
    if expressions[0] != '?':
        args['second'] = expressions[0]
    if expressions[1] != '?':
        args['minute'] = expressions[1]
    if expressions[2] != '?':
        args['hour'] = expressions[2]
    if expressions[3] != '?':
        args['day'] = expressions[3]
    if expressions[4] != '?':
        args['month'] = expressions[4]
    if expressions[5] != '?':
        args['day_of_week'] = expressions[5]
    return args


def add_(func=None, args=None, kwargs=None, key=None, name=None, trigger='cron', cron=None):
    scheduler.add_job(func=func, args=args, kwargs=kwargs, id=str(key), name=name, trigger=trigger, **_cron(cron))


# 删除任务
def delete_(key):
    scheduler.remove_job(str(key))


# 暂停任务
def pause_(key):
    scheduler.pause_job(str(key))


# 启动存在的任务
def start_(key):
    scheduler.remove_job(str(key))
