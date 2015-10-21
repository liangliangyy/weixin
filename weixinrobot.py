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
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import werobot
import gevent.monkey;
gevent.monkey.patch_all()
from werobot.reply import ArticlesReply, Article


robot = werobot.WeRoBot(token='lylinux')
import re
from Apis.bolg import *
from werobot.reply import ArticlesReply, Article

@robot.filter(re.compile(r"^\?.*"),re.compile(r"^\？.*"))
def search(message):

    s=message.content

    blogapi=blog()
    articles=blogapi.Search(str(s).replace('?','').replace('？',''))
    if len(articles) ==0:
        return str(s).replace('?','')+' 没有搜索到文章哦'
    reply = ArticlesReply(message=message)
    for article in articles:
        reply.add_article(article)

    return reply


#中文问号
def s(message):
    s=message.content
    blogapi=blog()
    ask='？'
    ask=ask.decode('utf-8')
    articles=blogapi.Search(str(s.replace(ask,'')))
    if len(articles) ==0:
        return str(s).replace('？','')+' 没有搜索到文章哦'
    reply = ArticlesReply(message=message)
    for article in articles:
        reply.add_article(article)

    return reply

@robot.text
def deal(message):
    ask='？'

    ask=ask.decode('utf-8')

    if message.content.find(ask)==0:
        return s(message)


@robot.subscribe
def sub(message):
    return '''欢迎关注!
    ?关键字搜索文章
    如?python
    help获得帮助'''



@robot.filter(re.compile('help',re.I))
def help(message):
    return """?关键字搜索文章
    如?python
    help获得帮助
    """



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