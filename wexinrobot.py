#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: wexinrobot.py
@time: 2015/10/20 22:06
"""

import werobot
import gevent.monkey;
gevent.monkey.patch_all()

robot = werobot.WeRoBot(token='lylinux')

@robot.handler
def echo(message):
    return 'Hello World!'

robot.run('gevent',port=8888)