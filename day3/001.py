#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

list_1 = [1,4,6,7,8,12,1,1]
list_1 = set(list_1)#去重
list_2 = [2,3,5]

print(list_1,type(list_1))
print(list_2,type(list_2))
print(list_1.intersection(list_2))#交集
print(list_1.union(list_2))#并集
print(list_1.difference(list_2))#差集
print(list_1.issubset(list_2))#子集
print(list_1.issuperset(list_2))#父集
print(list_1.symmetric_difference(list_2))#对称差集
print(list_1.isdisjoint(list_2))#判断是否有交集




