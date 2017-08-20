#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
c = dict.fromkeys([6,7,8],[1,{"name":"zhang"},444])
print(c)
c[6][1]["name"] = "zhanggenming"
print(c)

d = dict.fromkeys([6,7,8],2)
print(d)
d[6] = 33333333333333
print(d)