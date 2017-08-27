#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(5)
















