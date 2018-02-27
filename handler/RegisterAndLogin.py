# coding:utf-8

import re
from BaseRequestHandler import BaseRequestHadler
from log import Logger
from utils.session import Session


class RegisterHandler(BaseRequestHadler):
    """用户注册"""
    def post(self, *args, **kwargs):
        mobile = self.json_data.get("mobile")
        password = self.json_data.get("password")
        phoneCode = self.json_data.get("phonecode")
        if not all((mobile, password, phoneCode)):
            return self.write(dict(errno="2507", errmsg="参数错误"))
        try:
            real_phone_code = self.redisdb.get("sms_code_%s" % mobile)
        except Exception as e:
            Logger.loginstance().error("redis错误：%s" % e)
            return self.write(dict(errno="2502", errmsg="查询错误"))
        if not phoneCode==real_phone_code:
            return self.write(dict(errno="2502", errmsg="查询错误"))
        try:
            id = self.mysqldb.execute("insert into tb_user_info(user_mobile, user_passwd, user_name, user_gender) "
                                      "values(%s, %s, %s, %s)", mobile, password, u"用户%s" % mobile, 0)
        except Exception as e:
            Logger.loginstance().error("数据插入错误:%s", e)
            return self.write(dict(errno="2510", errmsg="数据插入错误"))
        if id:
            session = Session(self)
            session.data = self.json_data
            session.save()
            return self.write(dict(errno="0", errmsg="ok"))


class LoginHandler(BaseRequestHadler):
    """用户登录"""
    def post(self, *args, **kwargs):
        # 获取参数
        mobile = self.json_data.get("mobile")
        password = self.json_data.get("password")

        # 检查参数
        if not all([mobile, password]):
            return self.write(dict(errcode="2507", errmsg="参数错误"))
        if not re.match(r"^1\d{10}$", mobile):
            return self.write(dict(errcode="2508", errmsg="手机号错误"))

        # 检查秘密是否正确
        res = self.mysqldb.get("select user_id,user_name,user_passwd from tb_user_info where user_mobile=%(mobile)s",
                          mobile=mobile)
        # password = hashlib.sha256(password + config.passwd_hash_key).hexdigest()
        if res and res["user_passwd"] == unicode(password):
            # 生成session数据
            # 返回客户端
            try:
                self.session = Session(self)
                self.session.data['user_id'] = res['user_id']
                self.session.data['name'] = res['user_name']
                self.session.data['mobile'] = mobile
                self.session.save()
            except Exception as e:
                Logger.loginstance().error(e)
            return self.write(dict(errcode="0", errmsg="OK"))
        else:
            return self.write(dict(errcode="2509", errmsg="手机号或密码错误！"))

