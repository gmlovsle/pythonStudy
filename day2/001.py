#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang

'''import sys
print(sys.path)#打印环境变量
print(sys.argv)
print(sys.argv[2])'''

import os
cmd_res = os.system("dir")#执行命令，不保存结果
cmd_res2 = os.popen("dir").read()
print("-->",cmd_res)
print("-->",cmd_res2)

os.mkdir("new_dir")