#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a ,b= b,a + b
        n = n + 1
    return "done"
f = fib(10)
while True:
    try:
        x = next(f)
        print(x)
    except StopIteration as e:
        print("Generator return value:",e.value)
        break

# print("".ljust(50,"-"))
# def fibmin(min):
#     n,a,b = 0 ,100,55
#     while n < min:
#         print(a)
#         a,b = b,a-b
#         n = n + 1
#     return
# fibmin(10)

















