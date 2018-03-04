# coding:utf-8
import os
from handler.RequestHandler import *
from handler import VerifyCode, RegisterAndLogin, UserCenter
# from tornado.web import StaticFileHandler
from handler.BaseRequestHandler import StaticFileHandler
urls = [
    # (r'/', IndexHandler),
    (r'/api/image', VerifyCode.ImageCodeHandler),
    (r'/api/smscode', VerifyCode.PhoneCodeHandle),
    (r'/api/register', RegisterAndLogin.RegisterHandler),
    (r'/api/login', RegisterAndLogin.LoginHandler),
    (r'/api/check_login', RegisterAndLogin.CheckUserLoginHandler),
    (r'/api/profile/avatar', UserCenter.UserImageUpload),
    (r'/api/profile', UserCenter.UserInfoHandler),
    (r'/api/profile/name', UserCenter.UserNameUploadHandler),
    (r'/(.*?)$', StaticFileHandler, dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html")),
]