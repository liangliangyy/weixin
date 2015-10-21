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
from werobot.reply import ArticlesReply, Article


robot = werobot.WeRoBot(token='lylinux')
import re
from Apis.bolg import *
from werobot.reply import ArticlesReply, Article

@robot.filter(re.compile(r"^\?.*"))
def search(message):

    s=message.content

    blogapi=blog()
    articles=blogapi.Search(str(s).replace('?',''))
    return articles


@robot.subscribe
def sub(message):
    return '欢迎关注!'



@robot.filter('^help$')
def help(message):
    return """
    ?关键字搜索文章
    如?python
    """
#@robot.filter('?')



@robot.handler
def echo(message):
    reply = ArticlesReply(message=message)
    article = Article(
        title="使用django rest framework实现的小工具",
        description="使用django rest framework实现的小工具",
        img="http://www.lylinux.org/wp-content/uploads/2014/12/f.jpg",
        url="http://www.lylinux.org/%E4%BD%BF%E7%94%A8django-rest-framework%E5%AE%9E%E7%8E%B0%E7%9A%84%E5%B0%8F%E5%B7%A5%E5%85%B7.html"
    )
    reply.add_article(article)
    return reply

robot.run('auto',port=8888)