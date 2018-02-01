# coding:utf-8
import torndb
from tornado.options import options, define
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import config
import urls
import redis


define(name="port", type=int, help="Port Bind")


class BaseApplication(Application):
    def __init__(self, *args, **kwargs):
        super(BaseApplication, self).__init__(*args, **kwargs)
        self.db = torndb.Connection(**config.mysqlconn)
        self.redis = redis.StrictRedis(**config.redisconn)


def main():
    app = BaseApplication(urls.urls, **config.conf)
    cur_server = HTTPServer(app)
    cur_server.listen(config.port)
    IOLoop.current().start()


if __name__ == "__main__":
    main()


