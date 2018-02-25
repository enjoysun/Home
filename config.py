# coding:utf-8
import os

# 启动端口
port = 8000

# Applaction参数
conf = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "cookie_secret": "hnyfXS/qSJOGDfwJT7SoBxVEvpBnj0OonIZFLJKOIOQ=",
    "xsrf_cookies": False,
    "debug": True,
}

# mysql
mysqlconn = dict(host="127.0.0.1", database="house", user="root", password="123")

# redis
redisconn = dict(host="127.0.0.1", port=6379)

"""
关于日志记录：Python server.py --help查看记录日记配置参数
       使用tail -f 日志文件名可以在linux窗体实时查看写入日志 
       import logging 该模块是Python自带模块
       1.在终端打印运行日志时必须要开启optinos.pares_command_line()
"""

# logging级别
log_level = "warning"

# logging 地址
log_path = os.path.join(os.path.dirname(__file__), "logs")