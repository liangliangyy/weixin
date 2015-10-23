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
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import sys, urllib, urllib2, json
from urllib2 import HTTPError
from werobot.reply import Article
import random


class blog():
    def __init__(self):
        pass

    def GetJsons(self, url):
        res = self.UserAgent(url)
        jsons = json.loads(res, encoding='utf-8')
        return jsons

    def UserAgent(self, url):
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", \
                     "Referer": 'http://baidu.com/'}

        req = urllib2.Request(url, headers=i_headers)

        html = urllib2.urlopen(req).read()
        return html

    # jsons=json.loads(res,encoding='utf-8')

    """"title",
            "description",
            "img",
            "url"
    """
    ##解析文章数组
    def parsepost(self, postarr, total=0):
        articles = []
        count = 0

        for post in postarr:
            url = post['url']
            title = post['title']
            description = post['excerpt']
            attachments = post['attachments']

            img = ''
            if len(attachments) > 0:
                img = attachments[0]['url']
            else:
                img = 'http://www.lylinux.org/imgs/%s.jpg' % random.randrange(1, 8)
            article = Article(title=title, description=description, img=img, url=url)
            articles.append(article)
            # articles.append(description)
            count += 1
            if count == 10:
                break
            if total != 0 and count == total:
                break;
        return articles

    ##搜索文章
    def Search(self, searchstr):

        url = "http://www.lylinux.org/api/get_search_results/?search=" + searchstr

        jsons = self.GetJsons(url)
        articles = []
        posts = jsons['posts']
        count = 0
        if jsons['count'] == 0:
            return []
        articles = self.parsepost(posts)
        return articles

    ##获得最近文章
    def get_recent_posts(self):
        url = 'http://www.lylinux.org/api/get_recent_posts/'
        res = self.UserAgent(url)
        jsons = self.GetJsons(url)
        posts = jsons['posts']
        articles = self.parsepost(posts)
        return articles

    ##获得分类目录文章
    def get_category_posts(self, category):
        url = 'http://www.lylinux.org/api/get_category_posts/?slug=' + category

        try:
            jsons = self.GetJsons(url)
            posts = jsons['posts']
            articles = self.parsepost(posts)
            return articles
        except urllib2.HTTPError:
            return self.Search(category)

    ##获得分类目录
    def get_categorys(self):
        url = 'http://www.lylinux.org/api/get_category_index/'
        jsons = self.GetJsons(url)
        categories = jsons['categories']
        result = ''
        for cat in categories:
            result = result + u'分类目录:%s 文章数:%s\n' % (cat['title'], cat['post_count'])
        return result
