# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:54:58 2024

@author: EBFoundry
"""

import serial
import time


com = 'COM5'
### todo connect pi to serial
#com ='ttysomethingsomethin'


ser = serial.Serial(com,115200)

while True:
    # Turn left right Motors on
    ser.write(b'1')
    ser.write(b'4')
    time.sleep(3)

    # Turn left right Motors off
    ser.write(b'0')
    ser.write(b'0')
    time.sleep(1)
