# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import socket

client = socket.socket()   #声明socket类型，同时生成socket链接对象
client.connect(("localhost",9999))

while True:
    msg = input("=>:").strip()
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)
    print("recv:",data)

client.close()
