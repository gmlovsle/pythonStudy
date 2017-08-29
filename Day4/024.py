#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
import time

def decorator(func):
    print("This is the decorator.")
    def wrapper(*args,**kwargs):
        start_time = time.time()
        time.sleep(2)
        func(*args,**kwargs)
        stop_time = time.time()
        print("This function is uesed %ss." % (stop_time-start_time))
    return wrapper


@decorator
def test1():
    print("This is the test1.")

test1()