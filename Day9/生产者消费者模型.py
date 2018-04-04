# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

import threading,time

import queue

q = queue.Queue(maxsize=10)

def Producer(name):
    count = 1
    while True:
        q.put("Apple%s" %count)
        time.sleep(0.5)
        print("Has produced apple%s" %count)
        count += 1
def Consumer(name):
    while True:
        print("[%s] get [%s] and eat it..." %(name,q.get()))
        time.sleep(1)

p = threading.Thread(target=Producer,args = ("Gmlovsle",))
c = threading.Thread(target=Consumer,args = ("Liqiang",))

p.start()
c.start()
