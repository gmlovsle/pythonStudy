#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
def add(a,b,c):
    return c(a) + c(b)

res = add(-3,4,abs)
print(res)



