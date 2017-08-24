#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

f = open("011.txt","r")
f_new = open("011new.txt","w")
for line in f:
    if "三代" in line:
        line = line.replace("三代","3代")
    f_new.write(line)
f.close()
f_new.close()


























