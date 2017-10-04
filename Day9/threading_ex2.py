# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import threading

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n

    def run(self):
        print("running task",self.n)

t1 = MyThread("t1")
t2 = MyThread("t2")
t1.start()
t1.join() #=wait()  效果变成串行
t2.start()






