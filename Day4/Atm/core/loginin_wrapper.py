#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
def loginin_wrapper(func):
    def wrapper(*args,**kwargs):
        loginin = False
        while loginin == False:
            loginin = func()
        return loginin
    return wrapper

