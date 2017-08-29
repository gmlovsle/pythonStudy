#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

def producer(name):
    c = consumer('Gen')
    c2 = consumer('Ming')
    c.__next__()
    c2.__next__()
    print("%s开始准备做包子啦!"%name)
    for i in range(1,5):
        time.sleep(1)
        print("%s做了2个包子!"%name)
        c.send(i)
        c2.send(i)

producer("Zhang")











