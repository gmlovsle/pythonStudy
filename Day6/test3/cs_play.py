#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

class Role(object):
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self,gun_name):
        print("%s just buy %s" %(self.name,gun_name))

r1 = Role('Zhang','police','AK47') #生成一个角色
r2 = Role('Yang','terrorist','B22') #生成一个角色

r1.buy_gun("AK47")


