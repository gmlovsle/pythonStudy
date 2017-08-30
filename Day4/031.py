#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

# print(all([1,-1,3]))#判断是否全部为真。数字只要不是0都是真
# print(any([]))#只要有一个为真就为真。
# print(ascii([1,2,"张根铭"]))#编程ascii格式，将列表变成str
# print(bin(4))#转成二进制
# print(bool([]))#判断是否为boolean值
# print(bytes("abcde",encoding="utf-8"))
#
# b = bytearray("abcde",encoding="utf-8")#转换成ascii值
# print(b[0])
# b[0] = 50
# print(b)
# def aaa():pass
# print(callable(aaa))#判断是否可以调用   True
# print(chr(99))#返回ascii对应的值反应过来   c
# print(ord("c"))#将值返回成ascii   99
#
# print(exec("for i in range(10):print(i)"))#将字符串代码用起来
# print(dir())#查看有什么方法
#print(divmod(5,1))#返回商和余数
# def sayhi(n):
#     print(n)
#     for i in range(n):
#         print(i)
# sayhi(3)
# calc = lambda n:3 if n<4 else n
# print(calc(5))

# res = filter(lambda n:n>5,range(10))#过滤器
# for i in res:
#     print(i)

# res = map(lambda n:n*n*n,range(5))#对你传入的所有值进行处理
# for i in res:
#     print(i)

# res = [n*2 for n in range(5)]
# for i in res:
#     print(i)

# import functools
# res = functools.reduce(lambda x,y:x+y,range(10))#依次相加
# print(res)

# a = frozenset(set([1,2,3,4,5,6,1,2]))#冻结数组

# print(globals())#打印这个程序的所有全局变量
#
# print(hash("sdfd"))#将“sdfd”添加到映射


# print(hex(16))#转换成16进制

# def test():
#     local_var = 333
#     print(locals())#打印局部变量
#     print(globals())
# test()

# print(oct(8))#转换成8进制

# pow(2,3,5)#  2**3 % 5
#
# pow(2,3,)#  2**3

# print(round(1.23456789,3))#保留3位小数

# print(slice("adc d"," "))#切片

# a = {6:2,8:0,2:15}
# print(sorted(a.items()))#将无序的字典排序
# print(sorted(a.items(),key = lambda x:x[1]))#按照字典里面的哪里来排序

# a = [1,2,3,4,5]
# b = ["a","b","c","d"]
# for i in zip(a,b):
#     print(i)

