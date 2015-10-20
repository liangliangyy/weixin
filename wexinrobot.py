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


from werobot.reply import ArticlesReply, Article


@robot.handler
def echo(message):
    return [
        [
            "title",
            "description",
            "img",
            "url"
        ],
        [
            "逝去日子",
            "使用django rest framework实现的小工具",
            "http://www.lylinux.org/%E4%BD%BF%E7%94%A8django-rest-framework%E5%AE%9E%E7%8E%B0%E7%9A%84%E5%B0%8F%E5%B7%A5%E5%85%B7.html",
            "http://www.lylinux.org/%E4%BD%BF%E7%94%A8django-rest-framework%E5%AE%9E%E7%8E%B0%E7%9A%84%E5%B0%8F%E5%B7%A5%E5%85%B7.html"
        ]
    ]

robot.run('auto',port=8888)