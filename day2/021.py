#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
def coustomer(a):
    purch = open(purchased,"r")
    aas = purch.readlines()
    purch.close()
    a1 = []
    a2 = []
    for aa in aas:
        b1,b2 = aa.strip().split()
        a1.append(b1)
        a2.append(b2)
    if a in a1:
        q1 = []
        q2 = []
        ind = a1.index(a)
        q = a2[ind].split(".")
        for i in q:
            qq = i.split(",")
            q1.append(qq[0])
            q2.append(qq[1])
        qqq = []
        for i in range(len(q1)):
            qqq.append("%s共%s件" %(q1[i],q2[i]))
        print("你上次购买的商品有：%s" %qqq)
    m = open(bank,"r")
    ms = m.readlines()
    jj=[]
    kk=[]
    gg=[]
    mm=[]
    bought=[]
    bought1=[]
    bought2=[]
    flag = 1
    sss = 0
    for i in ms:
        j,k = i.strip().split()
        jj.append(j)
        kk.append(k)
        if j == a:
            money = int(k)
            inde = ms.index(i)
    m.close()
    g = open(goods,"r")
    g_lings = g.readlines()
    g.close()
    while flag == 1:
        for good in g_lings:
            ggg,mmm = good.strip().split()
            gg.append(ggg)
            mm.append(mmm)
            print("%s %s" %(g_lings.index(good)+1,good))
        buy = input("请输入你要买的商品编号，按q退出：")
        if buy == "q" or buy == "Q":
            kk[inde]= remain
            change = open(bank,"w")
            for l in range(len(jj)):
                change.write("%s %s\n" %(jj[l],kk[l]))
            change.close()
            flag = 0
            change2 = open(purchased,"a")
            g = ""
            for i in range(len(bought1)):
                g = g + "%s,%s." %(bought2[i],bought1[i])
            g = g[:-1]
            change2.write("%s %s\n" %(login,g))
        elif int(buy) >= len(g_lings):
            print("对不起，没有该商品")
        else:
            buy = int(buy)
            buy = buy - 1

            if gg[buy] in bought2:
                sss += 1
                sm = bought2.index(gg[buy])
                bbb = int(bought1[sm]) + 1
                bought[sm] = "%s共%s件" %(gg[buy],bbb)
                bought1[sm] = int(bought1[sm]) + 1
                print("".center(50,"-"))
                print("你购买的商品有：%s共%s件，你的余额为：%s" %(bought,sss,remain))
                print("".center(50,"-"))
            else:
                sss += 1
                bought.append("%s共%s件" %(gg[buy],1))
                bought2.append(gg[buy])
                remain = int(money) - int(mm[buy])
                print("".center(50,"-"))
                print("你购买的商品有：%s共%s件，你的余额为：%s" %(bought,sss,remain))
                print("".center(50,"-"))
                bought1.append(1)

def merchant(a):
    command = input("请输入你要做的操作，a增加商品，d删除商品，m修改商品信息：")
    if command == "a" or command == "A":
        flag = 1
        while flag == 1:
            cargo = input("请输入商品名字：")
            price = input("请输入该商品价格：")
            if price.isnumeric():
                with open(goods,"a") as cargos:
                    cargos.write("\n%s %s" %(cargo,price))
                cargos.close()
                s =input("货物添加成功。按q退出,任意键继续添加商品：")
                if s == "q" or s == "Q":
                    print("退出成功")
                    flag = 0
            else:
                print("对不起，你输入的格式不正确")
    elif command == "d" or command == "D":
        flag = 1
        while flag == 1:
            good = open(goods,"r")
            good_lines = good.readlines()
            for good_line in good_lines:
                print("%s %s" %(good_lines.index(good_line)+1,good_line))
            good.close()
            cargo = int(input("请输入你要删除的商品编号:"))
            if cargo > 0 and cargo <= len(good_lines):
                cargo -= 1
                new_goods = open(goods,"w")
                for i in range(len(good_lines)):
                    if i != cargo:
                        new_goods.write(good_lines[i])
                d_again = input("删除成功，按q退出，任意键继续删除商品：")
                if d_again == "q" or d_again == "Q":
                    print("退出成功")
                    flag = 0
            else:
                print("没有该商品")
    elif command == "m" or command == "M":
        flag = 1
        good = open(goods,"r")
        good_lines = good.readlines()
        good.close()
        while flag == 1:
            cargos = []
            prices = []
            for good_line in good_lines:
                i,j = good_line.strip().split()
                print("%s %s" %(good_lines.index(good_line)+1,good_line))
                cargos.append(i)
                prices.append(j)
            m = input("请输入你要修改的商品编号：")
            new_price = input("请输入该商品的新价格：")
            if m.isnumeric() and new_price.isnumeric():
                if m > 0 and m <=len(good_lines):
                    new_goods = open(goods,"w")
                    for k in range(len(good_lines)):
                        if (int(m) - 1) == k:
                            prices[k] = new_price
                        new_goods.write("%s %s\n" %(cargos[k],prices[k]))
                        good_lines[k] = "%s %s\n" %(cargos[k],prices[k])
                    new_goods.close()
                    m_again = input("修改成功，按q退出，任意键继续修改商品价格：")
                    if m_again == "q" or m_again == "Q":
                        print("退出成功")
                        flag = 0
                else:
                    print("你输入的格式有误")
            else:
                print("你输入的格式有误")






account = "021account.txt"
bank = "021bank.txt"
purchased = "021purchased.txt"
goods = "021goods.txt"

file1 = open(account,"r")
file1_lines = file1.readlines()
roles = []
account_numbers = []
passwords = []
for i in file1_lines:
    role,account_number,password = i.strip().split()
    roles.append(role)
    account_numbers.append(account_number)
    passwords.append(password)
file1.close()

flag = 1
while flag == 1:
    login = input("请输入账号：")
    passwd = input("请输入密码：")
    if login in account_numbers:
        i = account_numbers.index(login)
        if passwords[i] == passwd:
            if roles[i] == "customer":
                print("顾客账号登陆成功！")
                coustomer(login)
                flag = 0
            else:
                print("商家账号登陆成功！")
                merchant(login)
                flag = 0
        else:
            back= input("密码错误，回车重新输入或者q退出！")
            if back == "q" or back == "Q":
                flag =0
    else:
        create = input("该账号不存在，想要创建吗？y进行创建顾客账号，其余退出")
        if create == "y" or create == "Y":
            a = input("请输入电话：")
            if a in account_numbers:
                print("该账号已存在，请重新登陆")
            else:
                if a.isdecimal() and len(a) == 11:
                    p = input("请输入密码：")
                    b = input("请输入你的银行卡余额：")
                    print("创建并登陆成功")
                    with open(account,"a") as addaccount:
                        addaccount.write("\ncustomer %s %s"%(a,p))
                    with open(bank,"a") as addbank:
                        addbank.write("\n%s" %(b))
                    coustomer(a)
                    flag = 0
                else:
                    print("对不起，账号格式不对，自动退出")
                    flag = 0
        else:
            print("退出成功")
            flag = 0

