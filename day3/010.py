#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
'''f = open("010.txt","r+")#读写
f = open("010.txt","w+")#写读
f = open("010.txt","a+")#追加写读
f = open("010.txt","wb")#二级制'''
f = open("010.txt","rb")#二级制

print(f.readlines())
