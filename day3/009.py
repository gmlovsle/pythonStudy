#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

'''import sys,time

for i in range(100):
    sys.stdout.write("0")
    sys.stdout.flush()
    time.sleep(1)
'''
f = open("009.txt","a")
f.seek(10)#指针移动不影响truncate的截取
f.truncate(20)#从头开始截取20位