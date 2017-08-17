#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
import copy

person=["name",["saving",100]]

p1 = person[:]
p2 = person[:]

p1[0] = "zhang"
p2[0] = "geng"
print(p1)
print(p2)
p1[1][1] = 50
print(p1)
print(p2)
'''p1 = copy.copy(person)
print(p1)

p2 = person[:]
print(p2)

p3 = list(person)
print(p3)'''

