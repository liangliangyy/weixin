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

robot = werobot.WeRoBot(token='lylinux', enable_session=True)

import re
from werobot.reply import ArticlesReply, Article
from RobotHandle import RobotHandle


@robot.filter(re.compile(r"^\?.*"))
def search(message, session):
    s = message.content
    searchstr = str(s).replace('?', '')
    handle = RobotHandle(message, session)
    return handle.search(searchstr)


@robot.filter(re.compile(r'^category\s*$', re.I))
def category(message, session):
    handel = RobotHandle(message, session)
    return handel.get_category()


@robot.filter(re.compile(r'^recent\s*$', re.I))
def recent(message, session):
    handel = RobotHandle(message, session)
    return handel.get_recent_posts()


@robot.filter(re.compile('^category\-.*$', re.I))
def categorypost(message, session):
    handel = RobotHandle(message, session)
    cate = str(message.content).replace('Category', '').replace('category', '').replace('-', '')
    print(cate)
    return handel.get_category_posts(cate)


@robot.filter(re.compile('^weather\:.*$', re.I))
def weather(message, session):
    handel = RobotHandle(message, session)
    cate = str(message.content).replace('weather', '').replace('Weather', '').replace(':', '')
    print(cate)
    return handel.weather(cate)


@robot.filter(re.compile('^idcard\:.*$', re.I))
def idcard(message, session):
    handel = RobotHandle(message, session)
    cate = str(message.content).replace('idcard', '').replace('Idcard', '').replace(':', '')
    print(cate)
    return handel.idcard(cate)


"""
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



"""


@robot.text
def deal(message):
    content = message.content
    ask = '？'
    ask = ask.decode('utf-8')
    if message.content.find(ask) == 0:
        searchstr = str(content.replace(ask, ''))
        if searchstr == '':
            return '请在?后面加上要搜索的关键字哦'


@robot.subscribe
def sub(message):
    return '''欢迎关注!
    ?关键字搜索文章.
    如?python.
    category获得文章分类目录及文章数.
    category-***获得该分类目录文章
    如category-python
    recent获得最新文章
    help获得帮助.'''


@robot.filter(re.compile('help', re.I))
def help(message):
    return """?关键字搜索文章

    如?python
    help获得帮助
    """


@robot.text
@robot.handler
def echo(message,session):
    handel = RobotHandle(message, session)
    info=message.content
    return handel.tuling(info)



robot.run('auto', port=8888)





