#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: tuling.py
@time: 2015/10/4 2:17
"""


import sys, urllib, urllib2, json
from BaseApi import *
from urllib2 import HTTPError


class TuLing(BaseApi):
    def __init__(self,info):
        BaseApi.__init__(self)
        self.info=info
        self.__key__='2f1446eb0321804291b0a1e217c25bb5'
        self.__requrl__='http://www.tuling123.com/openapi/api?key=%s&info=%s&userid=%s' % (self.__key__,self.info,137762)
    def getdata(self):
        res=self.UserAgent2(self.__requrl__)

        try:

            jsons = json.loads(res, encoding='utf-8')

            return jsons
        except:
            return "err"