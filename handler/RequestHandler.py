# coding:utf-8
import json
from log import Logger
from BaseRequestHandler import BaseRequestHadler


class IndexHandler(BaseRequestHadler):
    def get(self, *args, **kwargs):
        loghelper = Logger()
        dbhelper = self.mysqldb
        user_info = dbhelper.query("select * from tb_user_info")
        loghelper.warning(str(user_info))
        self.write("oksss")