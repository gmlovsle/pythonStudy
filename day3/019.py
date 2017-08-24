#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
def calc(n):
    print(n)
    if n < 1:
        return 0
    return calc(int(n/5))
calc(100)








