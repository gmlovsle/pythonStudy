#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
import sys
print(sys.getdefaultencoding())

s = "你 好"
s1 = s.encode("utf-8")
print(s1)
s1 = s1.decode("utf-8")
print(s1)
s2 = s1.encode("gbk")
print(s2)
s3 = s2.decode("gbk")
print(s3)










