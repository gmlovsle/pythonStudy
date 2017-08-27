#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
import time
def foo(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("运行函数总共耗时%ss" %(stop_time-start_time))
def bar():
    time.sleep(1)
    print("In the Bar")
foo(bar)




