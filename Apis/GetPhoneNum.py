#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: PhoneNum.py
@time: 2015/10/2 17:23
"""


import sys, urllib, urllib2, json
from BaseApi import *
from urllib2 import HTTPError
from urllib import urlencode


class GetPhoneNum(BaseApi):
    def __init__(self,num):
        BaseApi.__init__(self)
        self.num=num
        self.requrl='http://apis.baidu.com/showapi_open_bus/mobile/find?num='+self.num

    def getdata(self):

        try:
            res=self.UserAgent(self.requrl)
            jsons=json.loads(res,encoding='utf-8')
            return jsons
        except HTTPError:
            errobj=[{
                'code':'500',
                'msg':u'超时',
            }]
            return errobj