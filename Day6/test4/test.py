#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"


class person:
    cn = "中国"
    def __init__(self,name,age,addr,life_value=100):
        self.name = name
        self.age = age
        self.addr = addr
        self.__life_value = life_value

    def __del__(self):
        print("over!!!!!!!!!")

    def show_status(self):
        print("name:%s age:%s life_value:%s"%(self.name,self.age,self.__life_value))

zgm = person("zgm",25,"sichuan")
zgm.show_status()






