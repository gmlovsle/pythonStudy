#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import shelve
import datetime

d = shelve.open("shelve_test")

info = {"age":25,"tel":18180820306}
name = ["zhanggenming","yangshenglan","wang"]

d["info"] = info
d["name"] = name
d["date"] = datetime.datetime.now()
d.close()



