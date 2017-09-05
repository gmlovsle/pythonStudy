#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import copy
a = {
    "18180820306":{"password":"123","money":10000},
    "18383382196":{"password":"123","money":10000}
     }
b = a.copy()

a["18180820306"]["money"] = 0

print(a)
print(b)
