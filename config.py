# coding:utf-8
import os

# 启动端口
port = 8000

# Applaction参数
conf = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "cookie_secret": "hnyfXS/qSJOGDfwJT7SoBxVEvpBnj0OonIZFLJKOIOQ=",
    "xsrf_cookies": "GsB89hkvRoup6MKYA9/vD+2X4QGV8E9irpTd27eYjY4=",
    # "debug": True,
}

# mysql
mysqlconn = dict(host="127.0.0.1", database="house", user="root", password="123")

# redis
redisconn = dict()