# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

import socket
client = socket.socket()

client.connect(("localhost",9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1000)
    print("",cmd_res_size)
    received_size = 0
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1000)
        received_size += len(data)
        print(data.decode())
    else:
        print("cmd res receive done...",received_size)
client.close()



