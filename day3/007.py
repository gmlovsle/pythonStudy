#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
f = open("007.txt","r",encoding="utf-8")
print(f.tell())#打印文件指针

print(f.readline())
print(f.tell())#打印文件指针
print(f.readline())
print(f.tell())
f.seek(17)#跳转到指针36
print(f.readline())#读一行
print(f.encoding)#打印字符编码集
print(f.read(5))#读5个
print(f.name)#打印文件名
print(f.seekable())#判断该文件指针可移
print(f.flush())#刷新。比如写文件，读到该文件刷新到硬盘
print(f.buffer)


