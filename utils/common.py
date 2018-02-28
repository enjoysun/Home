# coding:utf-8


def require_login(fun):
    """验证登录装饰器"""
    def wapper(requesthandler, *args, **kwargs):
        if requesthandler.check_user_login():
            fun(requesthandler, *args, **kwargs)
        else:
            requesthandler.write(dict(errno=1, errmsg="fales"))
    return wapper