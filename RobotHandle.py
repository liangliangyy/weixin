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
from Apis.bolg import *



class RobotHandle():
    def __init__(self,message):
        self.message=message


    #搜索博客文章
    def search(self,content):
        blogapi=blog()
        articles=blogapi.Search(content)
        if len(articles) ==0:
            return content+' 没有搜索到文章哦'
        reply = ArticlesReply(message=self.message)
        for article in articles:
            reply.add_article(article)

        return reply
    def get_category(self):
        blogapi=blog()
        categorys=blogapi.get_categorys()

        return categorys
    def get_recent_posts(self):
        blogapi=blog()

        articles= blogapi.get_recent_posts()
        reply = ArticlesReply(message=self.message)
        for article in articles:
            reply.add_article(article)
    def get_category_posts(self,category):
        blogapi=blog()
        articles=blogapi.get_category_posts(category)
        if len(articles)==0:
            return '没有找到文章哦,或许是您的拼写有误呢~~'
        reply = ArticlesReply(message=self.message)
        for article in articles:
            reply.add_article(article)
        return reply
