# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:07:49 2023

@author: admin
"""
import time 
import socket

HOST = "127.0.0.1"
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1)
            if not data:
                break
            print("Got data: {}".format(data))
            conn.sendall(b'ACK')
