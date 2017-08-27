#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

import time
def timmer(func):
    def warpper(*args,**kwarge):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("used: %s" %(stop_time-start_time))
    return warpper

@timmer
def test1():
    time.sleep(3)
    print("In the test1")

test1()












