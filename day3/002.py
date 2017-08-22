#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
list_1 = [1,4,6,7,8,12,14,1]
list_1 = set(list_1)
list_2 = [2,3,5,1]
list_2 = set(list_2)
print(list_1 & list_2)#交集
print(list_1 | list_2)#并集
print(list_1 - list_2)#差集
print(list_1 ^ list_2)#对称差集
