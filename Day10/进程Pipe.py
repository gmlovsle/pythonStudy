# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

from multiprocessing import Process,Pipe

def f(conn):
    conn.send([42,None,"hello"])
    print("from parent",conn.recv())
    conn.close()

if __name__ == "__main__":
    parent_conn,child_conn = Pipe()
    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.send("hello from parent")
    p.join()







