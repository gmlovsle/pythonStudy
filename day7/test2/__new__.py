# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

# class Foo(object):
#     def __init__(self,name):
#         self.name = name
#
# obj = Foo("zhanggenming")
#
# print(type(obj))
# print(type(Foo))

#下面是上面的原始，上面的对下面的封装

def func(self):
    print("hello %s %s" %(self.name,self.age))

def __init__(self,name,age):
    self.name = name
    self.age = age

Foo = type("Foo",(object,),{"talk":func,"__init__":__init__})

print(type(Foo))

obj = Foo("zhang",23)
obj.talk()