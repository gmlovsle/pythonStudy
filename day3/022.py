#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
def judge():
    a = input("请输入你要做的操作，s查询，a增加，d删除，c修改,q退出")
    if a == "s" or a == "S":
        b = search()
    elif a == "a" or a == "A":
        b = add()
    elif a == "d" or a == "D":
        b = delete()
    elif a == "c" or a == "C":
        b = change()
    elif a == "q" or a == "Q":
        return 0
    return b

def center(a):
    return a.center(20," ")

def judge2(a,b):
    c = input("请输入%s"%(a))
    d = a.index(c)
    if b == "*":
        print(lines[d])
    else:
        for i in range(len(b)):
            e = judge3(b[i])
            print("%s:%s" %(b[i],e[d]))

def judge3(a):
    if a == "staff_id":
        return staff_ids
    elif a == "name":
        return names
    elif a == "age":
        return ages
    elif a == "phone":
        return phones
    elif a == "dept":
        return depts
    elif a == "enroll_date":
        return enroll_dates

def search():
    a = input("请输入你要显示的项，输入staff_id/name/age/phone/dept/enroll_date，多项用','分开。显示全部用'*'表示")
    arr = a.split(",")
    for i in arr:
        if i == "staff_id" or i == "name" or i == "age" or i == "phone" or i == "dept" or i == "enroll_date" or i == "*":
            if i == "*":
                arr = "*"
            continue
        else:
            print("输入格式不正确，请重新输入")
            search()
            return
    b = input("请输入你要查询的项，输入staff_id/name/age/phone/dept/enroll_date，目前只能单项查询")
    if b == "staff_id":
        judge2(staff_ids,arr)
    elif b == "name":
        judge2(names,arr)
    elif b == "age":
        judge2(ages,arr)
    elif b == "phone":
        judge2(phones,arr)
    elif b == "dept":
        judge2(depts,arr)
    elif b == "enroll_date":
        judge2(enroll_dates,arr)
    else:
        print("输入错误。")
    c = input("是否继续？Y/N")
    if c == "N" or c == "n":
        return 0
    elif c == "Y" or c == "y":
        return 1

def add():
    f = open("022.txt","a")
    staff_id = len(staff_ids) + 1
    name = input("请输入name:")
    age = input("请输入age:")
    phone = input("请输入phone:")
    dept = input("请输入dept:")
    enroll_date = input("请输入enroll_date:")
    while phone == "":
        phone = input("请重新输入phone:")
    staff_ids.append(staff_id)
    names.append(name)
    ages.append(age)
    phones.append(phone)
    depts.append(dept)
    enroll_dates.append(enroll_date)
    f.write("\n%s,%s,%s,%s,%s,%s" %(staff_id,name,age,phone,dept,enroll_date))
    f.close()
    print("添加成功")
    c = input("是否继续？Y/N")
    if c == "N" or c == "n":
        return 0
    elif c == "Y" or c == "y":
        return 1

def delete():
    a = input("请输入你要删除的staff_id")
    f = open("022.txt","w")
    for line in lines:
        if int(a) != lines.index(line)+1:
            f.write(line)
    f.close()

def change():
    a = input("请输入你要修改的项name/age/phone/dept/enroll_date:")
    b = input("请输入你要删除的项的staff_id:")
    change = input("请输入你修改后的值：")
    c = judge3(a)
    b = int(b) - 1
    c[b] = change
    f = open("022.txt","w")
    for line in lines:
        if int(b) != lines.index(line):
            f.write(line)
        else:
            if c == names:
                f.write("%s,%s,%s,%s,%s,%s" %(b+1,change,ages[b],phones[b],depts[b],enroll_dates[b]))
            elif c == ages:
                f.write("%s,%s,%s,%s,%s,%s" %(b+1,names[b],change,phones[b],depts[b],enroll_dates[b]))
            elif c == phones:
                f.write("%s,%s,%s,%s,%s,%s" %(b+1,names[b],ages[b],change,depts[b],enroll_dates[b]))
            elif c == depts:
                f.write("%s,%s,%s,%s,%s,%s" %(b+1,names[b],ages[b],phones[b],change,enroll_dates[b]))
            elif c == enroll_dates:
                f.write("%s,%s,%s,%s,%s,%s" %(b+1,names[b],ages[b],phones[b],depts[b],change))

staff_ids = []
names = []
ages = []
phones = []
depts = []
enroll_dates = []
f = open("022.txt","r")
lines = f.readlines()
f.close()
flag = 1
for line in lines:
    staff_id,name,age,phone,dept,enroll_date = line.strip().split(",")
    staff_ids.append(staff_id)
    names.append(name)
    ages.append(age)
    phones.append(phone)
    depts.append(dept)
    enroll_dates.append(enroll_date)
while flag == 1:
    print("%s%s%s%s%s%s" %(center("staff_id"),center("name"),center("age"),center("phone"),center("dept"),center("enroll_date")))
    for i in range(len(staff_ids)):
        print("%s%s%s%s%s%s" %(center(staff_ids[i]),center(names[i]),center(ages[i]),center(phones[i]),center(depts[i]),center(enroll_dates[i])))
    flag = judge()











