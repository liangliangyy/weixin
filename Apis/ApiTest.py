#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'liangliangyy@gmail.com'

"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: ApiTest.py
@time: 2015/10/1 16:11
"""


from GetWeather import *
import json
from tuling import *

if __name__=='__main__':
    tl=TuLing("西安天气")
    print(tl.getdata())
    '''
    wearher=GetWeather('西安')
    res= wearher.getjson()

    #obj=[{'daily_forecast':[{'date':'','max':'','min':''}],'suject':''}]

    #res=str(res).decode('utf-8')
    jsons=json.loads(res,encoding='utf-8')
    print(str(res).decode('utf-8').encode(('gbk')))

    daily_forecast=jsons['HeWeather data service 3.0'][0]['daily_forecast']
    vs=jsons['HeWeather data service 3.0'][0]
    weathermodel=Weather()
    day=DailyModel()

    weathermodel.txt=vs['suggestion']['comf']['txt']
    weathermodel.brf=vs['suggestion']['comf']['brf']

    weatherlist=list()


    for daily in daily_forecast:
        """
        out=str(daily['date'])+' '+str(daily['wind']['dir'])
        fin=str(out).decode('utf-8').encode('gbk')
        print(str(out).decode('utf-8').encode('gbk'))
        """
        #print(daily['wind']['dir'])
        day.tmpmax=daily['tmp']['max']
        day.tmpmin=daily['tmp']['min']
        day.date=daily['date']
        day.winddir=daily['wind']['dir']
        day.windsc=daily['wind']['sc']
        day.pcpn=daily['pcpn']
        day.hum==daily['hum']
        day.pop=daily['pop']
        day.txt_d=daily['cond']['txt_d']
        day.txt_n=daily['cond']['txt_n']
        #weathermodel.daily_forecast.append(day)
        weatherlist.append(day)
    weathermodel.daily_forecast=tuple(weatherlist)
    print(len(weathermodel.daily_forecast))

    #data= WeatherSerializer(weathermodel)

    #print(data.data)
'''