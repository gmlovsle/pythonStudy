#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
list_1 = [1,4,6,7,8,12,14,1]
list_1 = set(list_1)
list_2 = [2,3,5,1]
list_2 = set(list_2)

list_1.add(999)
print(list_1)
list_1.update([123,456,789])
print(list_1)
list_1.remove(123)
print(list_1)

print(list_1 in list_2)#判断list_1是list_2成员
print(list_1 not in list_2)#判断list_1不是list_2成员
list_1.discard(4)#remove删除若没有会报错，discard不会
print(list_1.pop())#随机删除一个并返回该值

