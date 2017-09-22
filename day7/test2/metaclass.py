# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
class MyType(type):
    def __init__(self,*args,**kwargs):
        print("2")

    def __call__(self, *args, **kwargs):
        print("4")
        obj = self.__new__(self)
        self.__init__(obj,*args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("1")
        return type.__new__(cls, *args, **kwargs)

print("0")

class Foo(object,metaclass=MyType):

    def __init__(self,name):
        print("6")
        self.name = name

    def __new__(cls, *args, **kwargs):
        print("5")
        return object.__new__(cls)
print("3")
f = Foo("zhang")
print("7")





