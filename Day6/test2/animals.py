#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"


class Dog:

    def __init__(self,name):
        self.name = name

    def bulk(self):
        print("%s:wang wang wang!" %self.name)

d1 = Dog("li")
d2 = Dog("qiang")
d3 = Dog("qig")

d1.bulk()
d2.bulk()
d3.bulk()




