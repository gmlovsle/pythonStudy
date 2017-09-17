#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

#class people:经典类
class people(object):
    def __init__(self,name,age):
        pass
    def eat(self):
        pass

class man(people):
    def __init__(self,name,age,money):
        #people.__init__(self,name,age)   和下一句一样
        super(man,self).__init__(name,age)
        self.money = money
        print(self.money)

m1 = man(1,1,100)



