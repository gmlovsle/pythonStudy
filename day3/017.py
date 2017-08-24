#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
def test1(a,*a1):
    print(a)
    print(a1)
test1(1,2,3,4,5)
test1(*[1,2,3,4,5])


def test2(**b2):
    print(b2)
    print(b2["name"])
    print(b2["age"])
test2(name = "dkfjkd",age = 8,sex = "djk")
test2(**{"name":"dkfjkd","age":8,"sex":"djk"})







