#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import os,sys
from module_1 import logger as logger_module_1
from module_1 import name
def logger():
    print("logger in main")


logger()
logger_module_1()
print(name)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)
print(sys.path)