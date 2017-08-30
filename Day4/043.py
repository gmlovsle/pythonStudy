#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
__author__ = "Genming Zhang"

import pickle

def sayhi(name):
    print("hello,",name)

info = {
    "name":"Genming Zhang",
    "age":25,
    "func":sayhi
}
f = open("043.txt","wb")
f.write(pickle.dumps(info)) #  pickle.dump(info,f)
f.close()
