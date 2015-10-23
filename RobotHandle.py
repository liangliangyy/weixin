#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: RobotHandle.py
@time: 2015/10/23 22:34
"""
from werobot.reply import ArticlesReply, Article


class RobotHandle():
    def __init__(self,message):
        self.message=message


    #搜索博客文章
    def search(self,content):
        from Apis.bolg import *
        blogapi=blog()
        articles=blogapi.Search(content)
        if len(articles) ==0:
            return content+' 没有搜索到文章哦'
        reply = ArticlesReply(message=self.message)
        for article in articles:
            reply.add_article(article)

        return reply

