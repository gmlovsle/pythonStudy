# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

from multiprocessing import Process,Queue
import queue
import threading

def f(qq):
    qq.put([42,None,"hello"])

if __name__ == "__main__":
    q =Queue()
    #p = threading.Thread(target=f,)
    p = Process(target=f,args = (q,))
    p.start()
    print(q.get())