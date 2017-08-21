#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
b = []
c = []

q1 = []
q2 = []


a = "022.txt"
a1 = open(a,"r")
a2 = a1.readlines()
for i in a2:
    a3,a4 = i.strip().split()
    b.append(a3)
    c.append(a4)

if "18180820306" in b:
    ind = b.index("18180820306")
    d = c[ind].split(".")
    for i in d:
        qq = i.split(",")
        q1.append(qq[0])
        q2.append(qq[1])
print(q1)
print(q2)