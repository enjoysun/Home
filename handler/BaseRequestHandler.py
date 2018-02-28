# coding:utf-8
from tornado.web import RequestHandler, StaticFileHandler
from log import Logger
from utils.session import Session
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
        self.xsrf_token
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

    def check_user_login(self):
        self.session = Session(self)
        return self.session.data


class StaticFileHandler(StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token
