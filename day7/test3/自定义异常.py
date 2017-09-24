# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

class ZgmException(Exception):

    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise ZgmException("Zgm's exception")
except ZgmException as e:
    print(e)




