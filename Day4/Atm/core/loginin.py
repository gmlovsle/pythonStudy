#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

import json,os,time
from core import json_path
from core import loginin_wrapper
@loginin_wrapper.loginin_wrapper
def loginin():
    name = input("请输入你的账号：")
    json_paths = json_path.json_path(name)
    if os.path.isfile(json_paths):
        password = input("请输入密码：")
        with open(json_paths,"r") as f:
            messages = json.load(f)
            if messages["password"] == password:
                exp_time_stamp = time.mktime(time.strptime(messages["expire_date"], "%Y-%m-%d"))
                if exp_time_stamp < time.time():
                    print("\033[34;1m对不起，信用卡“%s”已过期，请重新申请。\033[0m" %(name))
                    return False
                else:
                    return messages
            else:
                print("密码错误！")
                return False
        f.close()
    else:
        print("\033[34;1m对不起，用户“%s”不存在。\033[0m" %(name))
        return False
