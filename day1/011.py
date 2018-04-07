#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

_username="zhanggenming"
_password="123456"
username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")

if username == _username and password == _password:
    print("Welcome",username,password,"login...")
else:
    print("Invalid username or password!")


