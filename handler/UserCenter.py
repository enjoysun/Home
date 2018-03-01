# coding:utf-8
from BaseRequestHandler import BaseRequestHadler
from log import Logger
from utils import image_upload, session


class UserImageUpload(BaseRequestHadler):
    """用户头像上传"""
    def post(self, *args, **kwargs):
        try:
            imagedata = self.request.files["avatar"][0]["body"]
        except Exception as e:
            Logger.loginstance().error("获取头像错误%s" % e)
            return self.write(dict(errno="2550", errmsg="false"))
        try:
            imagename = image_upload.imgupload(imagedata)
        except Exception as e:
            Logger.loginstance().error("上传七牛出错%s" % e)
            return self.write(dict(errno="2550", errmsg="false"))
        try:
            id = self.mysqldb.execute("update tb_user_info set user_img=%s where user_mobile=%s", imagename,
                                      self.session.data["mobile"])
        except Exception as e:
            Logger.loginstance().error("mysql错误：%s" % e)
            return self.write(dict(errno="2550", errmsg="false"))
        return self.write(dict(errno="1", errmsg="true", name=imagename))

