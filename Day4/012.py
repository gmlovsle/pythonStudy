#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
def decorator(func):
    def subdecorater(*args,**kwargs):
        func(*args,**kwargs)
        print("In the decoratror")
    return subdecorater

@decorator
def add(a,b):
    print(a + b)

@decorator
def subtract(a):
    print(a - 82)

@decorator
def multiply(a,b,c):
    print(a * b * c)

@decorator
def divide():
    print("In teh divide")

add(2,2)
subtract(100)
multiply(5,9,100)
divide()