#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"


def shop_choice(shop):
    for i in shop:
        print(i)
    flag = 1
    while flag == 1:
        a = input("请输入选择>>")
        if a == "q" or a == "Q":
            return 0,0
        if a in shop:
            if isinstance(shop[a],dict):
                return shop_choice(shop[a])
            else:
                return shop[a],a
        else:
            print("输入错误，请重新输入")