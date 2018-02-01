# coding:utf-8
from BaseRequestHandler import BaseRequestHadler
import json


class IndexHandler(BaseRequestHadler):
    def get(self, *args, **kwargs):
        dbhelper = self.mysqldb
        user_info = dbhelper.query("select * from tb_user_info")
        self.write(str(user_info))