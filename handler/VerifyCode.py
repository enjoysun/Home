# coding:utf-8

import constants
from log import Logger
from .BaseRequestHandler import BaseRequestHadler
from utils.captcha.captcha import captcha


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
