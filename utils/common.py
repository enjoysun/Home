# coding:utf-8
import functools
import json
import datetime


def require_login(fun):
    """验证登录装饰器"""
    @functools.wraps(fun)
    def wapper(requesthandler, *args, **kwargs):
        if requesthandler.check_user_login():
            fun(requesthandler, *args, **kwargs)
        else:
            requesthandler.write(dict(errno=4101, errmsg="fales"))
    return wapper


# json不支持对date和datetime序列化，需要重写json扩展
class MyJson(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(o, datetime.date):
            return o.strftime("%Y-%m-%d")
        return json.JSONEncoder.default(self, o)