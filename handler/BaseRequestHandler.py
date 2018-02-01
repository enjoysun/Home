# coding:utf-8
from tornado.web import RequestHandler


class BaseRequestHadler(RequestHandler):

    @property
    def mysqldb(self):
        return self.application.db

    @property
    def redisdb(self):
        return self.application.redis

    def prepare(self):
        pass

    def write_error(self, status_code, **kwargs):
        pass

    def initialize(self):
        pass

    def set_default_headers(self):
        pass

    def on_finish(self):
        super(BaseRequestHadler, self).on_finish()