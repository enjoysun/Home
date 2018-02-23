# coding:utf-8
import os
from handler.RequestHandler import *
from handler import VerifyCode
from tornado.web import StaticFileHandler
urls = [
    # (r'/', IndexHandler),
    (r'/api/image', VerifyCode.ImageCodeHandler),
    (r'/(.*?)$', StaticFileHandler, dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html")),
]