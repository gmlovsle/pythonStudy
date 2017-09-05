#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import json
from core import json_path
from core import shop_choice
def shopping(auth_data):
    money = auth_data["balance"]
    credit = auth_data["credit"]
    shop_path = json_path.json_path("shopping")
    name_path = json_path.json_path(auth_data["id"])
    with open(shop_path,"r",encoding="utf-8") as f:
        shop = json.load(f)
    f.close()
    flag = 1
    cart = []
    while flag == 1:
        print("你的账户余额为%s，信用额度为%s" %(money,credit))
        a,b = shop_choice.shop_choice(shop)
        if a == 0:
            flag = 0
            if len(cart) != 0:
                print("你本次购买的商品为%s，你的账户余额为%s，信用额度为%s" %(cart,money,credit))
                with open(name_path,"r") as f:
                    messages = json.load(f)
                f.close()
                with open(name_path,"w") as f2:
                    messages["balance"] = money
                    messages["credit"] = credit
                    json.dump(messages,f2)
                f2.close()
        else:
            if money + credit < a:
                print("余额及信用值不足，请充值。")
                flag = 0
            elif money < a:
                credit = credit - a + money
                money = 0
                print("购买%s成功" %(b))
                cart.append(b)
            else:
                money = money - a
                print("购买%s成功" %(b))
                cart.append(b)
