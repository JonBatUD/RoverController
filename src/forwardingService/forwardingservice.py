# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:54:58 2024

@author: EBFoundry
"""

import serial
import time
import socket

com = '/dev/ttyACM0'
### todo connect pi to serial
#com ='ttysomethingsomethin'


ser = serial.Serial(com,115200)
time.sleep(3)

import time 
import socket

HOST = "192.168.1.143"
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
            ser.write(data)
            msg = ser.readline()
            print(msg)
            #conn.sendall(b'ACK')
'''-
while True:
    # Turn left right Motors on
    print('sending forward 1')
    ser.write(b'1')
    msg = ser.readline()
    print(msg)
    time.sleep(5)


    # Turn left right Motors off
    print('sending stop 3')
    ser.write(b'3')
    msg = ser.readline()
    print(msg)

    time.sleep(1)

    print('sending forward 5')
    ser.write(b'5')
    msg = ser.readline()
    print(msg)
    time.sleep(5)

    print('sending stop 7')
    ser.write(b'7')
    msg = ser.readline()
    print(msg)
    time.sleep(1)
'''