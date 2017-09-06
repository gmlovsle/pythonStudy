#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

import configparser
config = configparser.ConfigParser()
config.read('example.ini')

print(config.defaults())
print(config["bitbucket.org"]["user"])

#删除
sec = config.remove_section("bitbucket.org")
config.write(open("example.cfg","w"))
