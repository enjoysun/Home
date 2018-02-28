# coding:utf-8
import uuid
import json
from log import Logger


class Session(object):
    """自定义session"""
    def __init__(self, request_handler):
        self.request_handler = request_handler
        # 判断是否是第一次设置
        self.session_id = self.request_handler.get_secure_cookie("sid")
        # 如果不存在sessionid则生成sessionid
        if not self.session_id:
            self.session_id = uuid.uuid4().get_hex()
            self.data = {}
            self.request_handler.set_secure_cookie("sid", self.session_id)
        # 存在则取值
        else:
            try:
                json_data = self.request_handler.redisdb.get("sess_%s" % self.session_id)
            except Exception as e:
                Logger.loginstance().error("redis错误%s"%e)
                raise Exception("redis read fail")
            if not json_data:
                self.data = {}
            else:
                self.data = json.loads(json_data)

    def save(self):
        try:
            self.request_handler.redisdb.setex("sess_%s"%self.session_id, 120, json.dumps(self.data))
        except Exception as e:
            Logger.loginstance().error("redis错误%s"%e)
            raise Exception("redis set fail")

    def clear(self):
        self.request_handler.set_header("sid", "")
        try:
            self.request_handler.redisdb.delete("sess_%s"%self.session_id)
        except Exception as e:
            Logger.loginstance().error("redis错误%s"%e)
            raise Exception("redis del fail")



