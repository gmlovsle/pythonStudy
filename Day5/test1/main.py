#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
from module import test

def logger():
    test()
    print("in the logger")

def search():
    test()
    print("in the search")

logger()
search()