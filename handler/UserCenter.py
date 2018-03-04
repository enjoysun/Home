# coding:utf-8
from BaseRequestHandler import BaseRequestHadler
from log import Logger
from utils import image_upload, session, common
import config


class UserImageUpload(BaseRequestHadler):
    """用户头像上传"""
    @common.require_login
    def post(self, *args, **kwargs):
        try:
            imagedata = self.request.files["avatar"][0]["body"]
        except Exception as e:
            Logger.loginstance().error("获取头像错误%s" % e)
            return self.write(dict(errno="4101", errmsg="false"))
        try:
            imagename = image_upload.imgupload(imagedata)
        except Exception as e:
            Logger.loginstance().error("上传七牛出错%s" % e)
            return self.write(dict(errno="4101", errmsg="false"))
        try:
            id = self.mysqldb.execute("update tb_user_info set user_img=%s where user_mobile=%s", imagename,
                                      self.session.data["mobile"])
        except Exception as e:
            Logger.loginstance().error("mysql错误：%s" % e)
            return self.write(dict(errno="4101", errmsg="false"))
        return self.write(dict(errno="0", errmsg="true", name=config.img_default_domain+imagename))


class UserInfoHandler(BaseRequestHadler):
    @common.require_login
    def get(self, *args, **kwargs):
        try:
            data_row = self.mysqldb.get("select * from tb_user_info where user_mobile=%s" % self.session.data["mobile"])
        except Exception as e:
            Logger.loginstance().error("mysql错误%s"%e)
            return self.write(dict(errno="4101", errmsg="false"))
        return self.write(dict(errno="0", errmsg="ok", data={"user_id": data_row["user_id"], "name": data_row["user_name"],
                                                             "mobile": data_row["user_mobile"],
                                                             "avatar": config.img_default_domain+data_row["user_img"]}))


class UserNameUploadHandler(BaseRequestHadler):
    @common.require_login
    def post(self, *args, **kwargs):
        try:
            id = self.mysqldb.execute("update tb_user_info set user_name='%s' where user_mobile=%s" % (self.json_data["name"],
                                                                                                     self.session.data["mobile"]))
        except Exception as e:
            Logger.loginstance().error("mysql错误%s"%e)
            return self.write(dict(errno="4001", errmsg="false"))
        return self.write(dict(errno="0", errmsg="ok"))



