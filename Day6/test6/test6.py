#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        print('%s: 喵喵喵!' %self.name)

class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' %self.name)

def func(obj):
    obj.talk()

c1 = Cat('小晴')
d1 = Dog('李磊')


func(c1)
func(d1)




