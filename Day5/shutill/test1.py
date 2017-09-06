#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import shutil
f1 = open("本节笔记",encoding="utf-8")

f2 = open("笔记2","w",encoding="utf-8")


shutil.copyfileobj(f1,f2)
shutil.copystat("本节笔记","笔记3")