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
from werobot.reply import ArticlesReply, Article
from RobotHandle import RobotHandle





@robot.filter(re.compile(r"^\?.*"))
def search(message):

    s=message.content
    searchstr=str(s).replace('?','')
    handle=RobotHandle(message)
    return handle.search(searchstr)


@robot.filter(re.compile(r'^category\s*$',re.I))
def category(message):
    handel=RobotHandle(message)
    return handel.get_category()


@robot.filter(re.compile(r'^recent\s*$',re.I))
def recent(message):
    handel=RobotHandle(message)
    return handel.get_recent_posts()

@robot.filter(re.compile('^category\-.*$',re.I))
def categorypost(message):
    handel=RobotHandle(message)
    cate=re.sub('^category\-\s*','',message.content,re.I)
    print(cate)
    return handel.get_category_posts(cate)



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
    content=message.content
    ask='？'
    ask=ask.decode('utf-8')
    if message.content.find(ask)==0:
        searchstr=str(content.replace(ask,''))
        if searchstr=='':
            return '请在?后面加上要搜索的关键字哦'



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
@robot.text



@robot.handler
def echo(message):
    print(message.content)
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