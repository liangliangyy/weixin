#!/usr/bin/env python
# encoding: utf-8

__author__ = 'liangliangyy@gmail.com'

"""
@version: 0.1
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: Weather.py
@time: 2015/10/1 16:00
"""

import sys, urllib, urllib2, json
from BaseApi import *
from urllib2 import HTTPError


class GetWeather(BaseApi):
    def __init__(self, city):
        BaseApi.__init__(self,'8dd1326fc4b271db91e03dba3d84b427')
        #BaseApi.__init__(self, 'd9b3201a8c8842a59e2dacb94f7fe12d')
        self.cityname = city
        self.requrl = 'http://apis.baidu.com/heweather/weather/free?city=' + self.cityname
        url='https://api.heweather.com/x3/weather?city=%s&key=%s' %(city,'d9b3201a8c8842a59e2dacb94f7fe12d')
        self.requrl=url

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
                    'qlty':'',
                    'city':'',
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
            weatherobj[0]['city']= jsons['HeWeather data service 3.0'][0]['basic']['city']
            weatherobj[0]['qlty']= jsons['HeWeather data service 3.0'][0]['aqi']['city']['qlty']
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
                #count += 1
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
            name=str(self.cityname).decode('utf-8')
            errobj = [{
                'code': '500',
                'msg': u'未找到'+name +u'城市天气信息',
            }]
            return errobj