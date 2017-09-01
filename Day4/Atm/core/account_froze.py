#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import json
def account_froze(count,messages,bank_path,name):
    if count < 3:
        print("验证失败，你还有\033[34;1m%s\033[0m次验证机会"%(3-count))
    else:
        print("你的账号已被锁定")
        with open(bank_path,"w") as f:
            messages[name]["status"] = "false"
            json.dump(messages,f)
        f.close()