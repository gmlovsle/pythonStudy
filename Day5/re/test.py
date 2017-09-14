#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import re
name = "zhange276841902genmming545gennnnnnn45gmlovsle520"
a = re.match("^zhang.\d+",name)
print(a.group())

b = re.search("ge.+ng",name)
print(b.group())

c = re.search("gen*",name)
print(c.group())

d = re.findall("gen*",name)
print(d)

e = re.findall("Bab|ABC","ABCBabcCD")
print(e)

f = re.split("([0-9]){3,100}","abcdefg1d132dfd5dfd")
print(f)

g = re.sub("[0-9]+","张","abc5dfd55fd222dfgj",count=2)
print(g)