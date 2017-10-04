# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"


import threading,time

def run(n):
    print("task",n)
    time.sleep(2)

start_time = time.time()
t_objs = []

for i in range(10):
    t =threading.Thread(target=run,args=("task %s"%i,))
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print(time.time() - start_time)
# t1 = threading.Thread(target=run,args = ("t1",))
# t1.start()
# t2 = threading.Thread(target=run,args = ("t2",))
# t2.start()

# run("t1")
# run("t2")