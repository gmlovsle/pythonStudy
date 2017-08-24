#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
def test1():
    print("test1")
def test2():
    print("test2")
    return 0
def test3():
    print("test3")
    return 1,"hello",["zhang","geng"],{1,2,3}
def test4():
    print("test4")
    return test2

x = test1()
y = test2()
z = test3()
m = test4()
print(x)
print(y)
print(z)
print(m)















