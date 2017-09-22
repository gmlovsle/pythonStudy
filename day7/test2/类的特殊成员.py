# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"


class Dog(object):
    '''__doc__打印部分'''
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("wocao",*args,**kwargs)

    def __str__(self):
        return "<obj:%s>" %self.name


print(Dog.__dict__)

print(Dog.__doc__)

d = Dog("xioa")
print(d.__dict__)
d()
print(d)
