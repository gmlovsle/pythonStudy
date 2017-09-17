#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

def person(name,age,sex,job):
    def walk(p):
        print("person %s is walking..." % p['name'])
    data = {
        'name':name,
        'age':age,
        'sex':sex,
        'job':job,
        'walk':walk
    }
    return data

def dog(name,dog_type):
    def bark(d):
        print("dog %s:wang.wang..wang..."%d['name'])
    data = {
        'name':name,
        'type':dog_type,
        'bark':bark
    }
    return data

d1 = dog("李磊","京巴")
p1 = person("严帅",36,"F","运维")
p2 = person("林海峰",27,"F","Teacher")
d1['bark'](p1) #把人的对象传给了狗的方法




