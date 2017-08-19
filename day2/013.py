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
print(info)
print(info["zhang"])
print("zhang3" in info)


info["ming"] = 1123467890
print(info)

print(info.get("zhang2"))

info.pop("zhang")   #删除
#del info["zhang"]  #删除
print(info)

info.popitem()#随机删除一个
print(info)














