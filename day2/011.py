#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

data = [
    ("手机",8000),
    ("电脑",4500),
    ("冰箱",2500),
    ("投影",3000),
    ("电视",6000),
    ("空调",18000),
]
shopping_list = []
salary = input("输入你的工资:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(data):
            print(index,item)
        user_choice = input("选择你要买的商品：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(data) and user_choice >=0:
                p_item = data[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("%s加入购物车,余额为\033[33;1m%s\033[0m" %(p_item,salary))
                else:
                    print("\33[31;1m你的余额只剩[%s]\033[0m" %salary)
            else:
                print("商品%s不存在，请重新输入" %user_choice)
        elif user_choice == "q":
            print("------物品清单------")
            for p in shopping_list:
                print(p)
            exit(print("你的余额为：",salary))
        else:
            print("请重新输入")
