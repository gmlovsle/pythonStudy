#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
__author__ = "Genming Zhang"
import json
f = open("041.txt","r")

data = json.loads(f.read())

print(data["age"])