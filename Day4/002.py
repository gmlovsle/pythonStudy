#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a + b
        n += 1
    return 'done'

for n in fib(6):
    print(n)



