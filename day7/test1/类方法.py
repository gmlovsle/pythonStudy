# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

class Dog(object):

    name = 333

    def __init__(self,name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s is eating "%(self.name))

d = Dog("Jack")
d.eat()




