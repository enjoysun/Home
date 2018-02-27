# coding:utf-8

import constants
import random
from log import Logger
from .BaseRequestHandler import BaseRequestHadler
from utils.captcha.captcha import captcha
from libs.tongxun import CCPInstance


class ImageCodeHandler(BaseRequestHadler):
    def get(self, *args, **kwargs):
        log = Logger()
        code_id = self.get_argument("codeid")
        pre_code_id = self.get_argument("pcodeid")
        if pre_code_id:
            try:
                self.redisdb.delete(pre_code_id) #手动删除验证码的codeid
            except Exception as e:
                log.error(e)
        name, text, image = captcha.generate_captcha()
        try:
            self.redisdb.setex("image_code_%s" % code_id, constants.PIC_CODE_EXPIRES_SECONDS, text)
        except Exception as e:
            log.error(e)
            self.write("")
        self.set_header("Content-Type", "image/jpg")
        self.write(image)


class PhoneCodeHandle(BaseRequestHadler):
    def post(self, *args, **kwargs):
        mobile = self.json_data.get("mobile", "")
        img_code_id = self.json_data.get("codeid", "")
        img_code_txt = self.json_data.get("codetxt", "")
        real_code_txt = None
        if not all((mobile, img_code_id, img_code_txt)):
            return self.write(dict(errno="2501", errmsg="参数错误"))
        try:
            real_code_txt = self.redisdb.get("image_code_%s" % img_code_id)
        except Exception as e:
            Logger.loginstance().error("redis错误:%s"%e)
            return self.write(dict(errno="2502", errmsg="查询错误"))
        if not real_code_txt:
            return self.write(dict(errno="2503", errmsg="验证码过期"))
        if str(real_code_txt).lower() != img_code_txt.lower():
            return self.write(dict(errno="2504", errmsg="验证码错误"))
        sms_code = "%04d"%random.randint(0, 9999)
        try:
            self.redisdb.setex("sms_code_%s" % mobile, constants.SMS_CODE_EXPIRES_SECONDS, sms_code)
        except Exception as e:
            Logger.loginstance().error("redis错误：%s"%e)
        try:
            CCPInstance.CCP.cppinstance().sendTemplateSMS(mobile, [sms_code, constants.SMS_CODE_EXPIRES_SECONDS], "1")
        except Exception as e:
            Logger.loginstance().error("短信发送失败:%s"%e)
            return self.write(dict(errno="2505", errmsg="短信发送失败"))
        return self.write(dict(errno="2506", errmsg="ok"))
