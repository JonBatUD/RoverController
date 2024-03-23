# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:28:33 2024

@author: admin

Rover controller 
get keyboard input
Send a byte 
"""

import socket
import time


HOST = '192.168.1.143'
PORT = 5555



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        time.sleep(1)
        
        try:
            # Get a key press
            # Send the coresponding byte
            s.send(b'1')
            msg = s.recv(3)
            print(msg)
            
        except KeyboardInterrupt:
            s.send(b'0')
            s.close()
            

