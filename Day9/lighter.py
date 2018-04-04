# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"


import time
import threading

event = threading.Event()

def lighter():
    count = 0
    event.set()
    while True:
        if count >= 5 and count < 8:
            event.clear()
            print("\033[41;1mRed light is on...\033[0m")
        elif count > 8:
            event.set()
            count = 0
        else:
            print("\033[44;1mGreen light is on...\033[0m")
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            print("[%s] running..." %name)
            time.sleep(1)
        else:
            print("[%s] saw red light,waiting..." %name)
            event.wait()
            print("\033[34;1m[%s] sgreen light is on ,start going...\033[0m" %name)

light = threading.Thread(target=lighter,)
light.start()
car1 = threading.Thread(target=car,args=("Benchi",))
car1.start()

