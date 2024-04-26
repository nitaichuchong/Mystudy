from urllib.parse import urljoin

from qiniu import Auth, put_file, etag

from swiper import config
from worker import call_by_worker

QN_AUTH = Auth(config.QN_AK, config.QN_SK)


def get_qn_url(filename):
    '''获取文件 url '''
    return urljoin(config.QN_BASE_URL, filename)


def upload_to_qiniu(localfile, key, ):
    '''
    将本地文件上传到七牛云

    Args:
        localfile: 本地文件位置
        key: 上传到云服务器后的文件名
    '''

    #生成上传 Token，可以指定过期时间等
    token = QN_AUTH.upload_token(config.QN_BUCKET, key, 3600)

    ret, info = put_file(token, key, localfile, version='v2')

    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)

    url = get_qn_url(key)

    return ret, info, url

async_upload_to_qiniu = call_by_worker(upload_to_qiniu)