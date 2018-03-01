# coding:utf-8
from qiniu import Auth, put_file, etag, urlsafe_base64_encode, put_data
import qiniu.config


def imgupload(image_data):
    """文件上传七牛，返回文件名"""
    if not image_data:
        return None
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'T9MninEy6Jqr17SESI6is9cEIUv9hzaP52Javv-r'
    secret_key = 'wHmNJz397XEwrBUSJIfu75lBNBdwbGZvTIiwFxJP'
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = 'home'
    # 上传到七牛后保存的文件名
    # key = 'my-python-logo.png';
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)
    # 要上传文件的本地路径
    # localfile = './sync/bbb.jpg'
    ret, info = put_data(token, None, image_data)
    # print(info)
    # assert ret['key'] == key
    # assert ret['hash'] == etag(localfile)
    return ret['key']


if __name__ == "__main__":
    """
    raw_input:无论终端输入值，都返回字符串
    input:会以python表达式和语法来解析终端的输入
    """
    filename = raw_input("文件路径")
    try:
        fileinstance = open(filename, 'rb')
        qiniuname = imgupload(fileinstance.read())
        print qiniuname
    except Exception as e:
        print e