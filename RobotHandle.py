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
from werobot.reply import ArticlesReply, Article, MusicReply
from Apis.bolg import *


class RobotHandle():
    def __init__(self, message, session):
        userid = message.source
        self.userid = userid

        try:
            count = session[userid]
            count = count + 1
            session[userid] = count
        except:
            session[userid] = 0
        self.message = message

        self.session = session

    def helpinfo(self):
        return '''欢迎关注!
        默认会与图灵机器人聊天~~
    你可以通过下面这些命令来获得信息
    ?关键字搜索文章.
    如?python.
    category获得文章分类目录及文章数.
    category-***获得该分类目录文章
    如category-python
    recent获得最新文章
    help获得帮助.
    weather:获得天气
    如weather:西安
    idcard:获得身份证信息
    如idcard:61048119xxxxxxxxxx
    music:音乐搜索
    如music:阴天快乐
    PS:以上标点符号都不支持中文标点~~求轻喷~~~
    '''

    # 搜索博客文章
    def search(self, content):
        blogapi = blog()
        articles = blogapi.Search(content)
        if len(articles) == 0:
            return content + ' 没有搜索到文章哦'
        reply = ArticlesReply(message=self.message)
        for article in articles:
            reply.add_article(article)

        return reply

    def get_category(self):
        blogapi = blog()
        categorys = blogapi.get_categorys()
        return categorys

    def get_recent_posts(self):
        blogapi = blog()
        articles = blogapi.get_recent_posts()
        reply = ArticlesReply(message=self.message)
        for article in articles:
            reply.add_article(article)
        return reply

    def get_category_posts(self, category):
        blogapi = blog()
        articles = blogapi.get_category_posts(category)
        if len(articles) == 0:
            return '没有找到文章哦,或许是您的拼写有误呢~~'
        reply = ArticlesReply(message=self.message)
        for article in articles:
            reply.add_article(article)
        return reply

    def weather(self, cityname):
        from Apis.GetWeather import GetWeather

        weather = GetWeather(cityname)

        result = weather.getdata()
        data = result[0]
        if data['code'] == '500':
            return data['msg']

        res = '污染度:%s  舒适度:%s 建议:%s \n未来%s天天气预报:\n' % (data['qlty'], data['brf'], data['txt'], len(data['daily']))
        for daily in data['daily']:
            # 天气  最高温度  最低温度 降水概率
            res = res + '日期:%s 天气:%s 最高温度:%s 最低温度:%s 降水概率:%s\n' % (
                daily['date'], daily['cond']['txt_n'], daily['tmp']['max'], daily['tmp']['min'], daily['pop'])

        return res

    def idcard(self, idcard):
        from Apis.GetIdCard import GetIdCard

        card = GetIdCard(idcard)
        cardinfo = card.getdata()

        if cardinfo['errNum'] == -1:
            return cardinfo['retMsg']
        data = cardinfo['retData']
        sex = "女"
        if data['sex'] == "M":
            sex = "男"
        return '性别:%s 出生年月:%s 地址:%s' % (sex, data['birthday'], data['address'])

    def checkcount(self):
        return False

    def tuling(self, info):

        from Apis.tuling import TuLing

        tl = TuLing(info)
        info = tl.getdata()
        if not self.checkcount():
            return info['text']
        else:
            return self.helpinfo()

    def music(self, search):
        from Apis.music import Music

        m = Music(search)
        res = m.getData()
        if res['status'] == 'failed':
            return '咩有找到你要找到音乐哦'

        music = res['data']['data']['list'][0]

        item=[]

        item.append(music['songName'])
        item.append(music['albumName'])
        item.append(music['songUrl'])
        return item