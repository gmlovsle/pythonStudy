# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import os,multiprocessing

def info(title):
    print(title)
    print("module name:",__name__)
    print("parent process ID:",os.getppid())
    print("process ID:",os.getpid())

def f(name):
    info("\033[33;1mCalled from child process function f\033[0m")
    print("hello",name)

if __name__ == "__main__":
    info("\033[34;1mCalled from process function info\33[0m")
    p = multiprocessing.Process(target=f,args=("Gmlovsle",))
    p.start()

