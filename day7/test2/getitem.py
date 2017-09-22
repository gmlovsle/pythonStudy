# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

class Foo(object):
    def __init__(self):
        self.data = {}

    def __getitem__(self, item):
        print("__getitem__",item)

    def __setitem__(self, key, value):
        print("__setitem__",key,value)
        self.data[key] = value

    def __delitem__(self, key):
        print("__delitem__",key)

obj = Foo()

obj["name"] = "zhanggenming"

print(obj.data)

