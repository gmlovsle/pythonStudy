#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

class Dog(object):

    def __init__(self,name):
        self.name = name

    @staticmethod #静态方法
    def eat(self):
        print("%s is eating "%(self.name))

d = Dog("Jack")
d.eat(d)
