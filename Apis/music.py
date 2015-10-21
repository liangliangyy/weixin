#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: music.py
@time: 2015/10/8 20:06
"""


import sys, urllib, urllib2, json
from BaseApi import *
from urllib2 import HTTPError


class Music(BaseApi):
    def __init__(self,query):
        BaseApi.__init__(self)
        self.query=query
        self.requrl= 'http://apis.baidu.com/geekery/music/query?s='+self.query+'&limit=10&p=1'


    def getData(self):
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