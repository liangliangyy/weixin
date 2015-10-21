#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: ocrImg.py
@time: 2015/10/4 12:20
"""


import sys, urllib, urllib2, json
from BaseApi import *
from urllib2 import HTTPError


class ocrImg():
    def __init__(self,imgbytes):
        self.imgbytes=imgbytes


    def getdata(self):
        url = 'http://apis.baidu.com/apistore/idlocr/ocr'
        data = {}
        data['fromdevice'] = "pc"
        data['clientip'] = "111.192.76.68"
        data['detecttype'] = "LocateRecognize"
        data['languagetype'] = "CHN_ENG"
        data['imagetype'] = "1"
        data['image']=self.imgbytes
        decoded_data = urllib.urlencode(data)
        req = urllib2.Request(url, data = decoded_data)
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
        req.add_header("apikey", "8dd1326fc4b271db91e03dba3d84b427")

        resp = urllib2.urlopen(req)
        content = resp.read()
        #if(content):
         #   print(content)

        content = json.loads(content)
        res=''
        for line in content['retData']:
	        res=res+ line['word']
        return res