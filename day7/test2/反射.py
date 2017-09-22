# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
def bulk(self):
    print("%s is yelling...."%self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating %s" %(self.name,food))

d = Dog("Liqiang")
choice = input(">>:").strip()

if hasattr(d,choice):
    func = getattr(d,choice)
    func("baba")
else:
    setattr(d,choice,bulk)
    func = getattr(d,choice)
    func(d)