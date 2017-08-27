#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
from collections import Iterable
print(isinstance([], Iterable))

print(isinstance({}, Iterable))

print(isinstance('abc', Iterable))

print(isinstance((x for x in range(10)), Iterable))

print(isinstance(100, Iterable))#判断对象是否是一个Iterable可迭代对象

from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
'''
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
'''