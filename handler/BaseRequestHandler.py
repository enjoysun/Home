# coding:utf-8
from tornado.web import RequestHandler, StaticFileHandler
from log import Logger
import json


class BaseRequestHadler(RequestHandler):

    @property
    def logger(self):
        return Logger()

    @property
    def mysqldb(self):
        return self.application.db

    @property
    def redisdb(self):
        return self.application.redis

    def prepare(self):
        """预解析json"""
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_data = json.loads(self.request.body)
        else:
            self.json_data = {}

    def write_error(self, status_code, **kwargs):
        pass

    def initialize(self):
        pass

    def set_default_headers(self):
        """设置默认header为json"""
        self.set_header("Content-type", "application/json;charset=UTF-8")

    def on_finish(self):
        super(BaseRequestHadler, self).on_finish()


class StaticFileHandler(StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token
