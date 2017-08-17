#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

a = "张根铭".encode("utf-8")
print(a)

b = b'\xe6\x9d\xa8\xe8\x83\x9c\xe8\x93\x9d\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'.decode("utf-8")
print(b)

c = "张根铭"
print(c)
print(c.encode("utf-8"))
print(c.encode(encoding="utf-8"))
print(c.encode("utf-8").decode("utf-8"))
print(c.encode(encoding="utf-8").decode(encoding="utf-8"))