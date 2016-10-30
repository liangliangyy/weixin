#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: Apache Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.org/
@software: PyCharm
@file: CommonHelper.py
@time: 2016/10/30 下午4:22
"""

import redis
import json


class StringHelper():
    @staticmethod
    def GetMD5(s):
        import hashlib
        hash_md5 = hashlib.md5(s)
        return hash_md5.hexdigest()

    @staticmethod
    def WriteLog(logpath, content):
        with open(logpath, 'a') as file:
            file.writelines(content)


class RedisHelper():
    def __init__(self, redishost='192.168.21.130', password=None):
        # redishost = '192.168.21.130'
        # password = 'lylinuxRedis'
        if password:
            self.__redis__ = redis.Redis(host=redishost, password=password)
        else:
            self.__redis__ = redis.Redis(host=redishost)

    def sset(self, key, obj):
        value = json.dumps(obj)
        return self.__redis__.sadd(key, value)
