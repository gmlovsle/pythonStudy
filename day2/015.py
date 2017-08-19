#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

info = {
    "zhang":1,
    "geng":222,
    "dkfd":5252,
    "df":122,
    "dfdfdfdaaa":12222,
}
b = {
    "zhang":12345,
    "sheng":12398888,
    2:3,
}
info.update(b)

c = dict.fromkeys([6,7,8],"monke")#初始化一个新的字典
print(c)
print(info)
print(info.items())#把字典转成列表

