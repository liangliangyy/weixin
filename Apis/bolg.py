#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: bolg.py
@time: 2015/10/21 21:46
"""
import sys, urllib, urllib2, json
from urllib2 import HTTPError
from werobot.reply import  Article
import random


class blog():
    def __init__(self):
        pass

    def UserAgent(self, url):
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", \
                     "Referer": 'http://baidu.com/'}

        req = urllib2.Request(url,headers=i_headers)

        html = urllib2.urlopen(req).read()
        return html
    #jsons=json.loads(res,encoding='utf-8')

    """"title",
            "description",
            "img",
            "url"
    """
    def Search(self,searchstr):
        url="http://www.lylinux.org/api/get_search_results/?search="+searchstr
        res=self.UserAgent(url)
        jsons=json.loads(res,encoding='utf-8')
        articles=[]
        posts=jsons['posts']
        count=0
        if jsons['count']==0:
            return []
        for post in posts:
            url=post['url']
            title=post['title']
            description=post['excerpt']
            attachments=post['attachments']

            img=''
            if len(attachments)>0:
                img=attachments[0]['url']
            else:
                img='http://www.lylinux.org/imgs/%s.jpg' % random.randrange(1,8)
            article=Article(title=title,description=description,img=img,url=url)
            articles.append(article)
            count+=1
            if count==10:
                break
        return articles


