#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
import time
def customer(name):
    print("%s is ready to eating apples." %(name))
    while True:
        pingguo = yield
        print("The apple【%s】is eated by %s." %(pingguo,name))

def producer(name):
    a = customer("Genming Zhang")
    a.__next__()
    for i in range(1,6):
        time.sleep(2)
        print("%s is taking off the apple 【%s】 from the tree." %(name,i))
        a.send(i)

producer("Shenglan Yang")










