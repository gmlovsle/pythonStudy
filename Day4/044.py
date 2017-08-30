#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
__author__ = "Genming Zhang"

import pickle

def sayhi(name):
    print("hello,",name)
    print("hello2,",name)

f = open("043.txt","rb")

data = pickle.loads(f.read())# data = pickle.load(f)

data["func"]("Genming Zhang")