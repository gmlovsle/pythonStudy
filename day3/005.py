#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

f = open("005.txt","r")

for index,line in enumerate(f.readlines()):
    if index == 2:
        print("-------我是分割线-------")
        continue
    print(line.strip())

#低效
