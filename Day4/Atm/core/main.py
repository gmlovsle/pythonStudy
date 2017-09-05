#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

from conf import settings
from core import loginin
from core import next_month
from core import cash_out
from core import change
from core import pay_back
from core import recharge
from core import shopping
from core import transfer

def run():
    count = 0
    if settings.DATABASE["login"] == True:
        pass
        print("你的账号已经登陆")
    else:
        login = loginin.loginin(count)
        settings.DATABASE["login"] == False
        if login != False:
            print("你的本月账单为：\033[34;1m%s\033[0m元，剩余额度为\033[34;1m%s\033[0m元，还款截至日期为\033[34;1m%s\033[0m"\
            %(login["balance"],login["credit"]-login["balance"],next_month.next_month(login["pay_day"])))
            while True:
                options = input("1充值，2购物，3套现，4还款，5转账，6更改账户信息，其余退出")
                if options == "1":
                    recharge.recharge(str(login["id"]))
                elif options == "2":
                    shopping.shopping(login)
                elif options == "3":
                    cash_out.cash_out()
                elif options == "4":
                    pay_back.pay_back()
                elif options == "5":
                    transfer.transfer()
                elif options == "6":
                    change.change()
                else:
                    return False