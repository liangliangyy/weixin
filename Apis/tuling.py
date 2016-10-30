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

from urllib2 import HTTPError


class TuLing():
    def __init__(self, info):

        self.info = info
        self.__key__ = '2f1446eb0321804291b0a1e217c25bb5'
        self.__requrl__ = 'http://www.tuling123.com/openapi/api?key=%s&info=%s&userid=%s' % (
            self.__key__, self.info, 137762)

    def UserAgent(self, url):
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", \
                     "Referer": 'http://baidu.com/',
                     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
                     }

        req = urllib2.Request(url)

        html = urllib2.urlopen(req).read()
        return html

    def getdata(self):
        res = self.UserAgent(self.__requrl__)
        try:
            jsons = json.loads(res, encoding='utf-8')
            return jsons
        except:
            return "err"
