# coding:utf-8

from CCPRestSDK import REST
import ConfigParser


accountSid = '8aaf07086178588a0161c85f8ce10c14'
# 说明：主账号，登陆云通讯网站后，可在控制台首页中看到开发者主账号ACCOUNT SID。

accountToken = '9ba233e2d2824f24accb2b0276769d6c'
# 说明：主账号Token，登陆云通讯网站后，可在控制台首页中看到开发者主账号AUTH TOKEN。

appId = '8aaf07086178588a0161c85f8d3f0c1a'
# 请使用管理控制台中已创建应用的APPID。

serverIP = 'app.cloopen.com'
# 说明：请求地址，生产环境配置成app.cloopen.com。

serverPort = '8883'
# 说明：请求端口 ，生产环境为8883.

softVersion = '2013-12-26' # 说明：REST API版本号保持不变。

class CCP(object):
    """初始化"""
    def __init__(self):
        self.rest = REST(serverIP, serverPort, softVersion)
        self.rest.setAccount(accountSid, accountToken)
        self.rest.setAppId(appId)

    @classmethod
    def cppinstance(cls):
        """使用单例"""
        if not hasattr(cls, "_instance"):
            _instance = cls()
        return _instance

    def sendTemplateSMS(self, to, datas, tempId):
        self.rest.sendTemplateSMS(to, datas, tempId)


if __name__ == "__main__":
    """测试"""
    ccp = CCP.cppinstance()
    ccp.sendTemplateSMS('18868195887', ["i love you", "everyday"], "1")

