#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
import time
def timer(func):#timer(test1)
    def deco():
        start_time = time.time()
        func()  #test1()
        stop_time = time.time()
        print("%s" %(stop_time-start_time))
    return deco

@timer   #   test1 = timer(test1)
def test1():
    time.sleep(3)
    print("In the test1")

def test2():
    time.sleep(2)
    print("In the test2")


test1()























