# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

from multiprocessing import Process,Pool
import time,os

def Foo(i):
    time.sleep(1)
    print("In process",os.getpid())
    return i+100

def Bar(arg):
    print("-->exec done:",arg,os.getpid())

if __name__ =="__main__":

    pool = Pool(3)
    print("主进程",os.getpid())
    for i in range(8):
        #pool.apply(func=Foo,args=(i,))                     #串行
        pool.apply_async(func=Foo,args=(i,),callback=Bar)   #并行

    print("end")
    pool.close()
    pool.join()




