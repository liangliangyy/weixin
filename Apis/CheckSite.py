#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: CheckSite.py
@time: 2015/10/11 20:08
"""

import urllib2
from urllib2 import HTTPError
import os

cmd='/bin/sh /root/scripts/servicerestart.sh'

def check():
    try:
        req=urllib2.urlopen('http://www.lylinux.org/')
        code=req.getcode()
        rsp=req.read()
        if code!=200:
            raise HTTPError


    except urllib2.URLError:
        os.system(cmd)
    except urllib2.HTTPError:
        os.system(cmd)


if __name__=='__main__':
    check()