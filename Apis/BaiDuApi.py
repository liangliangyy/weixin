#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: Apache Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.org/
@software: PyCharm
@file: BaiDuApi.py
@time: 2016/10/30 下午3:53
"""

import sys, urllib, urllib2, json
import hashlib
from CommonHelper import *
from urllib2 import HTTPError


class BaseApi():
    def __init__(self, apikey=None):
        if apikey:
            self.apikey = apikey
        else:
            self.apikey = '8dd1326fc4b271db91e03dba3d84b427'

    def UserAgent(self, url):
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", \
                     "Referer": 'http://baidu.com/'}

        req = urllib2.Request(url, headers=i_headers)
        req.add_header("apikey", self.apikey)
        html = urllib2.urlopen(req).read()
        return html

    def UserAgent2(self, url):
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", \
                     "Referer": 'http://baidu.com/',
                     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
                     }

        req = urllib2.Request(url)

        html = urllib2.urlopen(req).read()
        return html


apikey = '8dd1326fc4b271db91e03dba3d84b427'


class Weather(BaseApi):
    def __init__(self, city):
        BaseApi.__init__(self, apikey)
        self.cityname = city
        self.requrl = 'http://apis.baidu.com/heweather/weather/free?city=' + self.cityname
        url = 'https://api.heweather.com/x3/weather?city=%s&key=%s' % (city, 'd9b3201a8c8842a59e2dacb94f7fe12d')
        self.requrl = url

    def getjson(self):
        weatherobj = self.getdata()
        encodejson = json.dumps(weatherobj, ensure_ascii=False)
        encodejson = str(encodejson.encode('utf-8'))
        return encodejson

    def getdata(self):
        # return self.UserAgent(self.requrl)

        try:

            res = self.UserAgent2(self.requrl)

            jsons = json.loads(res, encoding='utf-8')

            daily_forecast = jsons['HeWeather data service 3.0'][0]['daily_forecast']
            vs = jsons['HeWeather data service 3.0'][0]

            dailyobj = [
                {
                    'tmpmax': '',
                    'tmpmin': '',
                    'date': '',
                    'winddir': '',
                    'windsc': '',
                    'pcpn': '',
                    'hum': '',
                    'pop': '',
                    'txt_d': '',
                    'txt_n': ''
                }
            ]

            weatherobj = [
                {
                    'code': '200',
                    'qlty': '',
                    'city': '',
                    'msg': '',
                    'txt': '',
                    'brf': '',
                    'daily': [
                        {

                        },
                    ],
                    'tmp': [
                        {

                        },
                    ]
                }
            ]

            weatherobj[0]['txt'] = vs['suggestion']['comf']['txt']
            weatherobj[0]['brf'] = vs['suggestion']['comf']['brf']
            weatherobj[0]['city'] = jsons['HeWeather data service 3.0'][0]['basic']['city']
            weatherobj[0]['qlty'] = jsons['HeWeather data service 3.0'][0]['aqi']['city']['qlty']
            dailylist = list()
            tmplist = list()
            count = 0
            for daily in daily_forecast:
                """
                dailyobj[0]['tmpmax']=daily['tmp']['max']
                dailyobj[0]['tmpmin']=daily['tmp']['min']
                dailyobj[0]['date']=daily['date']
                dailyobj[0]['winddir']=daily['wind']['dir']
                dailyobj[0]['windsc']=daily['wind']['sc']
                dailyobj[0]['pcpn']=daily['pcpn']
                dailyobj[0]['hum']=daily['hum']
                dailyobj[0]['pop']=daily['pop']
                dailyobj[0]['txt_d']=daily['cond']['txt_d']
                dailyobj[0]['txt_n']=daily['cond']['txt_n']
                """
                tmpobj = [
                    {
                        'date': '',
                        'tmpmax': '',
                        'tmpmin': ''
                    }
                ]
                tmpobj[count]['date'] = daily['date']
                tmpobj[count]['tmpmin'] = daily['tmp']['min']
                tmpobj[count]['tmpmax'] = daily['tmp']['max']
                # count += 1
                weatherobj[0]['daily'].append(daily)
                weatherobj[0]['tmp'].append(tmpobj)

            weatherobj[0]['daily'].remove(weatherobj[0]['daily'][0])
            weatherobj[0]['tmp'].remove(weatherobj[0]['tmp'][0])
            return weatherobj

            # encodejson=json.dumps(weatherobj,ensure_ascii=False)
            # encodejson=str(encodejson.encode('utf-8'))
            # return encodejson

        except HTTPError:
            errobj = [{
                'code': '500',
                'msg': u'超时',
            }]
            return errobj

        except KeyError:
            name = str(self.cityname).decode('utf-8')
            errobj = [{
                'code': '500',
                'msg': u'未找到' + name + u'城市天气信息',
            }]
            return errobj


class Joke(BaseApi):
    def __init__(self):
        self.badwords = [

            u"床",
            u"性",

            u"嘿",

            u"j",
            u"J",
            u"云雨",
            u"撸",
            u"公安",
            u"人民币",
            u"中国",
            u"寡妇",
            u"媳妇",
            u"高潮",
        ]

        BaseApi.__init__(self, apikey)
        self.requrl = "http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text"
        self.jokeindex = 1

    def __CheckBadWorld(self, content, bad):
        # content = str(content)
        return content.find(bad) >= 0

    def getjoke(self, page):
        content = self.__getjoke__(page).replace(' ', '')
        encodejson = json.loads(content, encoding='utf-8')
        # encodejson = str(encodejson)
        return encodejson

    def GetJokeContent(self):
        try:
            joke = self.getjoke(self.jokeindex)
            haserr = False
            for j in joke['showapi_res_body']['contentlist']:
                content = j["text"]
                for bad in self.badwords:
                    if self.__CheckBadWorld(content.encode('utf-8'), bad.encode('utf-8')):
                        haserr = True

            if not haserr:
                finalljoke = content.encode('utf-8')
                # print finalljoke
                return finalljoke
            else:
                self.jokeindex += 1
                return self.GetJokeContent()

        except Exception as e:
            # writefile(e.message)
            print(str(e.message))
            return self.GetJokeContent()

    def __getjoke__(self, page):
        url = self.requrl + "?page=" + str(page)
        res = self.UserAgent(url)
        return res


class WisdomWords(BaseApi):
    def __init__(self):
        BaseApi.__init__(self, apikey)
        self.__rediskey = 'wisdom'
        self.requrl = 'http://apis.baidu.com/txapi/dictum/dictum'

    def getWisdomWords(self):
        try:
            rsp = self.UserAgent(self.requrl)
            data = json.loads(rsp, encoding='utf-8')

            content = data['newslist'][0]['content']
            mrname = data['newslist'][0]['mrname']

            result = mrname + " : " + content
            if len(result) > 150:
                return self.getWisdomWords()
            md5 = StringHelper.GetMD5(result.encode('utf-8'))
            redishelper = RedisHelper()
            if redishelper.sset(self.__rediskey, md5) == 1:
                return result
            else:
                return self.getWisdomWords()

        except Exception, e:
            print e
            self.getWisdomWords()


class IDCard(BaseApi):
    def __init__(self, idcard):
        BaseApi.__init__(self, apikey)
        self.idcard = idcard
        self.requrl = 'http://apis.baidu.com/apistore/idservice/id?id=' + self.idcard

    def getdata(self):
        try:
            res = self.UserAgent(self.requrl)
            jsons = json.loads(res, encoding='utf-8')

            return jsons
        except HTTPError:
            errobj = [{
                'code': '500',
                'msg': u'超时',
            }]
            return errobj


class PhoneNum(BaseApi):
    def __init__(self, num):
        BaseApi.__init__(self, apikey)
        self.num = num
        self.requrl = 'http://apis.baidu.com/showapi_open_bus/mobile/find?num=' + self.num

    def getdata(self):

        try:
            res = self.UserAgent(self.requrl)
            jsons = json.loads(res, encoding='utf-8')
            return jsons
        except HTTPError:
            errobj = [{
                'code': '500',
                'msg': u'超时',
            }]
            return errobj


class Music(BaseApi):
    def __init__(self, query):
        BaseApi.__init__(self, apikey)
        self.query = query
        self.requrl = 'http://apis.baidu.com/geekery/music/query?s=' + self.query + '&limit=10&p=1'

    def getData(self):
        try:
            res = self.UserAgent(self.requrl)
            jsons = json.loads(res, encoding='utf-8')
            return jsons
        except HTTPError:
            errobj = [{
                'code': '500',
                'msg': u'超时',
            }]
            return errobj


if __name__ == '__main__':
    weather = Weather('上海')
    print weather.getdata()
