#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
salary = int(input("请输入你的工资："))
flag = 1
c=[]
count = 0
while flag==1:
    list = "007.txt"
    price = open(list,"r")
    price = price.readlines()
    a=[]
    b=[]
    print("---------------------------")
    for i in price:
        print(i)
        a1,a2,a3 = i.strip().split()
        a4=int(a3)
        b.append(a2)
        a.append(a4)
        count += 1
    print("---------------------------")
    s = input("你还想继续购买吗？Y/N")
    if s == "y" or s== "Y":
        buy = int(input("输入你想购买的商品编号："))
        if buy > count or buy < 0:
            print("没有该商品，请重新输入")
        else:
            if salary >= a[buy]:
                print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
                salary = salary -a[buy]
                print("你的余额为：",salary)
                c.append(b[buy])
                print("你购买的商品有：",c)
                print("↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
                continue
            else:
                print("余额不足")
                flag = 0
    elif s == "n" or s== "N":
        flag = 0
    else:
        print("输入错误，请重新输入")

