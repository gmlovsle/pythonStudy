#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
import time
user,passwd = "123","123"
def auth(auth_type):
    def out_wrapper(func):
        def wrapper(*args,**kwargs):
            print(wrapper)
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if username == user and password == passwd:
                    print("\33[32;1mUser login in!\33[0m")
                    res = func(*args,**kwargs)#res = home()
                    return res
                else:
                    print("\33[31;1mInvalid username or password!\33[0m")
            elif auth_type == "ldap":
                print("Connecting on web!")
        return wrapper
    return out_wrapper

def index():
    print("Welcome to index page！")

@auth(auth_type = "local")
def home():
    print("Welcome to home page！")
    return "home"

@auth(auth_type = "ldap")
def bbs():
    print("Welcome to bbs page！")

index()
print(home(5))
bbs()







