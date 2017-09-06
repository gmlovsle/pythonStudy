#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import shelve
import datetime

d = shelve.open("shelve_test")
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))




