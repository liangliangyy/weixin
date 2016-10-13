#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: Apache Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.org/
@software: PyCharm
@file: CommandHandler.py
@time: 2016/10/13 下午9:06
"""

import os

class CommandHandler():
    def __init__(self,Command):
        self.Command=Command
    @staticmethod
    def GetHelp():
        return """reboot:重启
                  wordpress:提交wordpress代码
                  ngrok:打开ngrok服务
                  vpn：重启vpn服务
        """
    def RunCommand(self):
        if self.Command=='':
            return
        #self.Command='ls'
        if self.Command.upper()=='REBOOT':
            return self.__run(' /usr/bin/python /root/scripts/LinodeHelper.py ')
        elif  self.Command.upper()=='WORDPRESS':
            return self.__run('cd /var/www/wordpress/ && git add . && git commit -m "test" && git push')
        elif self.Command.upper()=='NGROK':
            return self.__run('/root/scripts/ngrok.sh > /dev/null 2>&1 &')
        elif self.Command.upper()=='VPN':
            return self.__run('/bin/sh /root/scripts/vpnrestart.sh ')
        else:
            return self.__run(self.Command)

    def __run(self,runcommand):
        print 'ss'+runcommand
        str = os.popen(runcommand).read()
        return str
