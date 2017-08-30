#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
__author__ = "Genming Zhang"

import json

def sayhi(name):
    print("hello,",name)

info = {
    "name":"Genming Zhang",
    "age":25,
}
f = open("041.txt","w")
f.write(json.dumps(info))
f.close()







