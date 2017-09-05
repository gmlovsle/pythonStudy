#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

from core import json_path
from core import account_detection
from core import account_froze
import json
def recharge(name):
    count_password = 0
    count_phone = 0
    bank_path = json_path.json_path("bank")
    with open(bank_path,"r") as f:
        messages = json.load(f)
    f.close()
    active = account_detection.account_detection(messages,name)
    if active == "true":
        while count_password < 3:
            password = input("请输入密码：")
            if messages[name]["password"] == password:
                while count_phone < 3:
                    phone = input("请输入您的银行卡绑定的手机号进行验证：")
                    if messages[name]["phone"] == phone:
                        recharge_num = int(input("请输入你要充值的金额："))
                        if messages[name]["money"] < recharge_num:
                            print("你好\033[34;1m%s\033[0m，你的余额仅为\033[34;1m%s\033[0m元，无法完成\033[34;1m%s\033[0m元充值" \
                            %(name,messages[name]["money"],recharge_num))
                        else:
                            with open(bank_path,"w") as f:
                                messages[name]["money"] = messages[name]["money"] - recharge_num
                                json.dump(messages,f)
                            f.close()
                            print("充值到账户\033[34;1m%s\033[0m成功，账户余额\033[34;1m%s\033[0m元"\
                            %(name,messages[name]["money"]))
                            auth_path = json_path.json_path("%s"%name)

                            with open(auth_path,"r") as f2:
                                messages2 = json.load(f2)
                            f2.close()
                            with open(auth_path,"w") as f2:
                                messages2["balance"] = messages2["balance"] + recharge_num
                                json.dump(messages2,f2)
                            f2.close()
                    else:
                        count_phone += 1
                        account_froze.account_froze(count_phone,messages,bank_path,name)
                        if count_phone >=3:
                            return
            else:
                count_password += 1
                account_froze.account_froze(count_password,messages,bank_path,name)
                if count_password >=3:
                    return
    else:
        print("请先联系276841902@qq.com进行解锁。")
