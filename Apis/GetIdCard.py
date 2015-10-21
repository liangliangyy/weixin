#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: GetIdCard.py
@time: 2015/10/2 16:41
"""


import sys, urllib, urllib2, json
from BaseApi import *
from urllib2 import HTTPError

class GetIdCard(BaseApi):
    def __init__(self,idcard):
        BaseApi.__init__(self)
        self.idcard=idcard
        self.requrl='http://apis.baidu.com/apistore/idservice/id?id='+self.idcard



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



