import hashlib
import random
import time

import requests
from django.core.cache import cache

from common.errors import VcodeExist
from worker import call_by_worker
from swiper import config


def gen_verify_code(length=6):
    '''产生验证码'''
    min_value = 10 ** (length - 1)
    max_value = 10 ** length
    number = random.randrange(min_value, max_value)
    return number


def send_verify_code(phonenum):
    '''发送验证码'''

    key = f'VCode-{phonenum}'
    if not cache.has_key(key):
        vcode = gen_verify_code()
        send_sms(phonenum, vcode)
        cache.set(key, vcode, 300)

    else:
        raise VcodeExist

@call_by_worker
def send_sms(phonenum, vcode):
    '''发送短信'''
    url = 'https://api.netease.im/sms/sendcode.action'
    AppKey = config.WY_AppKey
    AppSecret = config.WY_AppSecret
    # 生成128个长度以内的随机字符串
    nonce = hashlib.new('sha512', str(time.time()).encode("utf-8")).hexdigest()
    # 获取当前时间戳
    curtime = str(int(time.time()))
    # 根据要求进行SHA1哈希计算
    check_sum = hashlib.sha1((AppSecret + nonce + curtime).encode("utf-8")).hexdigest()
    header = {
        "AppKey": AppKey,
        "Nonce": nonce,
        "CurTime": curtime,
        "CheckSum": check_sum
    }
    data = {
        'mobile': phonenum,  # 手机号
        'authCode': vcode,  # 自定义生成的验证码，代替云信官方的生成

    }
    resp = requests.post(url, data=data, headers=header)

    return resp



def check_vcode(phonenum, vcode):
    '''检查验证码'''
    cached_vcode = cache.get(f'VCode-{phonenum}')
    print(vcode, cached_vcode)
    return cached_vcode == vcode
