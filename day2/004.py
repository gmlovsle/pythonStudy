#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

name =["zhang","gen","ming","yang","sheng","lan"]
print(name)
print(name[0])
print(name[0:2])
print(name[-1])
print(name[-2:-1])
print(name[-2:])
print(name[::2])
name[0]= "@@@"
name.append("张")
name.insert(1,"jhjhjh")
print(name)
name.remove("gen")
print(name)
del name[-1] #del name[0]=name.pop(0)
print(name)
name.pop()
print(name)
print(name.index("yang"))
print(name[name.index("yang")])

name.reverse()
print(name)
name.sort()
print(name)
name.append("ming")
print(name.count("ming"))


name2 = [1,2,3,4]
name.extend(name2)

print(name,name2)
del name2
import copy
name3=name.copy()#浅copy,只copy第一层
print("-->",name3)
name4=[1,2,3,4,[0,5,6,7],8]
name5=name4.copy()
print(name4)
print(name5)
name6 = copy.deepcopy(name4)

name4[2]="dfdfd"
name4[4][3] = "aaaa"
print(name4)
print(name5)
print(name6)
name.clear()
print(name)

name11 = ["zhang","gen","ming","yang","sheng","lan"]
for i in name11:
    print(i)