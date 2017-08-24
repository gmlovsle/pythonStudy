#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
import time

def aaa():
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)
    with open("015.txt","a") as f:
        f.write("\n%s追加内容" %(time_current))

def test1():
    print("test1")
    aaa()
def test2():
    print("test2")
    aaa()
def test3():
    print("test3")
    aaa()

test1()
test2()
test3()







