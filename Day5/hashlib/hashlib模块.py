#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import hashlib

m = hashlib.md5()
m.update("张根铭".encode(encoding="utf-8"))
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())


s2 = hashlib.sha1()
s2.update(b"Hello")
print(s2.hexdigest())


