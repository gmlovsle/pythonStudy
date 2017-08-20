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

for name in info:
    print(name,info[name])
print("----------------")
for i,j in info.items():
    print(i,j)