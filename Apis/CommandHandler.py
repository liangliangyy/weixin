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
import jsonpickle


class CommandConfig():
    def __init__(self):
        self.Command = ''
        self.Desc = ''
        self.Name = ''

    def SetValues(self, dict):
        self.Command = dict['Command']
        self.Desc = dict['Desc']
        self.Name = dict['Name']


def GetConfigInfo():
    with open(os.path.join(os.path.dirname(__file__), 'CommandInfos.json'), 'r') as file:
        datas = file.readlines()
        str = ' '.join(datas)
        configs = jsonpickle.decode(str)
        for dict in configs:
            config = CommandConfig()
            config.SetValues(dict)
            yield config


class CommandHandler():
    def __init__(self, Command):
        self.Command = Command
        self.CommandConfigs = GetConfigInfo()

    def GetHelp(self):
        infos = []
        for c in self.CommandConfigs:
            infos.append(c.Name + ': ' + c.Desc)
        return '\n'.join(infos)

    def RunCommand(self):
        if self.Command == '':
            return
        # self.Command='ls'
        """
        if self.Command.upper() == 'REBOOT':
            return self.__run(' /usr/bin/python /root/scripts/LinodeHelper.py ')
        elif self.Command.upper() == 'WORDPRESS':
            return self.__run('cd /var/www/wordpress/ && git add . && git commit -m "test" && git push')
        elif self.Command.upper() == 'NGROK':
            return self.__run('/root/scripts/ngrok.sh > /dev/null 2>&1 &')
        elif self.Command.upper() == 'VPN':
            return self.__run('/bin/sh /root/scripts/vpnrestart.sh ')
        else:
            return self.__run(self.Command)
        """
        for config in self.CommandConfigs:
            if config.Name.upper()==self.Command.upper():
                return self.__run(config.Command)
        return self.__run(self.Command.lower())
    def __run(self, runcommand):
        try:
            str = os.popen(runcommand).read()
            return str
        except:
            return '命令执行出错!'
