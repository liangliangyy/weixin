#!/usr/bin/env python
# encoding: utf-8

__author__ = 'liangliangyy@gmail.com'

"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: BaseApi.py
@time: 2015/10/1 16:04
"""
import urllib2
"""
import socks
import socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",1080)
socket.socket =socks.socksocket
"""

class BaseApi():
    def __init__(self,apikey=None):
        if apikey:
            self.apikey=apikey
        else:
            self.apikey='8dd1326fc4b271db91e03dba3d84b427'

    def UserAgent(self, url):
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", \
                     "Referer": 'http://baidu.com/'}

        req = urllib2.Request(url,headers=i_headers)
        req.add_header("apikey",self.apikey)
        html = urllib2.urlopen(req).read()
        return html



    def UserAgent2(self,url):
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", \
                     "Referer": 'http://baidu.com/',
                     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
                     }


        req = urllib2.Request(url)

        html = urllib2.urlopen(req).read()
        return html