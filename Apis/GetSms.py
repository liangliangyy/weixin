#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: GetSms.py
@time: 2015/10/2 16:56
"""
import sys, urllib, urllib2, json
from BaseApi import *
from urllib2 import HTTPError
from urllib import urlencode


class GetSms(BaseApi):
    def __init__(self, mobile, content):
        BaseApi.__init__(self)
        data = {
            'content': content,
            'mobile': mobile
        }

        requrl = 'http://apis.baidu.com/sms_net/sms_net_sdk/sms_net_sdk?' + urlencode(data)

        self.requrl = requrl

    def getdata(self):
        res = self.UserAgent(self.requrl)
        jsons = json.loads(res, encoding='utf-8')
        return jsons

        try:
            res = self.UserAgent(self.requrl)
            jsons = json.loads(res, encoding='utf-8')
            return jsons
        except HTTPError:
            errobj = [{
                'code': '500',
                'msg': u'超时',
            }]
            return errobj
