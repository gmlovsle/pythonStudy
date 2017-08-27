#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
import time
def bar():
    time.sleep(1)
    print("In the bar.")

def test2(func):
    print(func)
    return func

#print(test2(bar))
bar = test2(bar)
bar()