# coding:utf-8
import os
from handler.RequestHandler import *
from handler import VerifyCode, RegisterAndLogin
# from tornado.web import StaticFileHandler
from handler.BaseRequestHandler import StaticFileHandler
urls = [
    # (r'/', IndexHandler),
    (r'/api/image', VerifyCode.ImageCodeHandler),
    (r'/api/smscode', VerifyCode.PhoneCodeHandle),
    (r'/api/register', RegisterAndLogin.RegisterHandler),
    (r'/api/login', RegisterAndLogin.LoginHandler),
    (r'/(.*?)$', StaticFileHandler, dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html")),
]