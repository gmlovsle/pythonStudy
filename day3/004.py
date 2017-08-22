#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

f = open("004.txt","r",encoding="utf-8")
datas = f.readlines()
datas2 = f.readlines()
for data in datas:
    print(data)
f.close()

w = open("004.txt","w")
w.write("dfdfdfdfdf")
w.close()

a = open("004,txt","a")
a.write("\ndfdfdfd!!!!!!!!")
a.close()






