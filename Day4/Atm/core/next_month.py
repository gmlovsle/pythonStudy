#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

import time

def next_month(pay_day):
    m = time.strftime("%m", time.localtime())
    y = time.strftime("%Y", time.localtime())
    if m == 12:
        y = int(y) + 1
    else:
        m = int(m) + 1
    return ("%s-%s-%s" %(y,m,pay_day))



