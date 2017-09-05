#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import os
def json_path(name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = r"%s\db\accounts\%s.json" %(base_dir,name)
    return path


