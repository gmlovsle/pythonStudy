# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

class Dog(object):

    def __init__(self,name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print("%s is eating %s"%(self.name,self.__food))

    @eat.setter
    def eat(self,food):
        print("set to food:",food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("delete")

d = Dog("Jack")
d.eat
d.eat = "baba"
d.eat

del d.eat



