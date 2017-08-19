#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
name = "zhang\tgenming is {name} and i am {year} old2"
print(name.capitalize())#首字母大写
print(name.count("g"))#统计有多少个g
print(name.center(50,"-"))#不够50在两边补-
print(name.endswith("2"))#是否是！！结尾
print(name.expandtabs(tabsize=10))#\t至第10位
print(name[name.find("g"):])#找到第一个g，截取
print(name.format(name="zzzz",year=23))#把name,year传回name
print(name.format_map({"name":"zh","year":"12"}))#把name,year传回name
print(name.index("g"))#g的第一个索引
print("ab23".isalnum()) #是否只包含数字和字母
print("abA".isalpha()) #是否是纯英文字符
print("1A".isdecimal()) #是否是十进制
print("1A".isdigit()) #是否是整数
print("a1A".isidentifier()) #是否是合法的标识符
print("a".islower()) #是否是小写
print("A".isupper()) #是否是大写
print("a".isnumeric()) #是否是数字
print("a".isspace()) #是否是空格
print("My Name".istitle()) #是否是标题
print("My Name".isprintable()) #是否能打印  tty file,drive file不能打印
print("+".join(["1","2","3","4"]))#用+串起来
print(name.ljust(50,"*"))#不够50在后面补*
print(name.rjust(50,"*"))#不够50在前面补*
print(name.lower()) #大写变小写
print(name.upper()) #小写变大写
print("\nZhang".lstrip())#去掉左边的非打印标识
print("Zhang\n".rstrip())#去掉右边的非打印标识

p = str.maketrans("abcdef","123456")
print("Zhanggenming".translate(p))#按照p的规则进行转码

print("Zhanggenming".replace("g","G",2))#把前面2个g换成G
print("Zhanggen ming".rfind("g"))#返回最右边的g的下标
print("Zhanggen ming".split("g"))#用g分隔
print("Zhanggen\n ming".splitlines())#按换行符分隔
print("Zhanggen ming".swapcase())#首字母小写，其余全部大写
print("zhang djk ddddG".title())#变成标题
print("zhanggenming".zfill(50))#左侧用0补齐50位

