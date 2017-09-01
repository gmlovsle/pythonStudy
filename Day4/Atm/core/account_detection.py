#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

def account_detection(messages,name):
    if messages[name]["status"] == "true":
        return "true"