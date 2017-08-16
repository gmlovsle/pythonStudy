#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

lock = r"015lock.txt"
data = r"015data.txt"
data2 = r"015data2.txt"

count = 0
flag = 1
lock_user = []

f1 = open(lock,"r")
lock_lines = f1.readlines()
f1.close()
for lock_line in lock_lines:
    lock_line = lock_line.strip("\n")
    lock_user.append(lock_line)

f2 = open(data,"r")
data_lines = f2.readlines()
f2.close()

f3 = open(data2,"r")
data2_lines = f3.readlines()
f3.close()

while flag == 1:
    name = input("Name:")
    password = input("Password:")
    if name in lock_user:
        cc = input("User is locked!Do you want to clear? Y/N")
        if cc == "Y" or cc == "y":
            ccphone = input("Telephone:")
            for j in data2_lines:
                n2,t2 = j.strip().split()
                if name == n2 and ccphone == t2:
                    print("Clear!")
                    f1 = open(lock,"r")
                    lock_lines = f1.readlines()
                    handle = open(lock,"w")
                    for lock_line in lock_lines:
                        lock_line = lock_line.strip("\n")
                        if lock_line != name:
                            handle.write(lock_line+"\n")
                        lock_user = []
                        f1 = open(lock,"r")
                        lock_lines = f1.readlines()
                        for lock_line in lock_lines:
                            lock_line = lock_line.strip("\n")
                            lock_user.append(lock_line)
    else:
        _name=[]
        for i in data_lines:
            n1,p1 = i.strip().split()
            _name.append(n1)
        if name in _name:
            count += 1
            if count > 2:
                print("Locked!")
                with open(lock,"a") as f:
                    f.write("\n" + name)
                    flag = 0
                break
            else:
                for i in data_lines:
                    n1,p1 = i.strip().split()
                    if name == n1 and password == p1:
                        print("Welcome login!")
                        flag = 0
        else:
            new = input("Do you want to creat one? Y/N")
            if new =="Y" or new == "y":
                telephone = input("Telephone:")
                with open(data,"a") as ff1:
                    ff1.write("\n" + name + " " + password)
                with open(data2,"a") as ff2:
                    ff2.write("\n" + name + " " + telephone)
                break