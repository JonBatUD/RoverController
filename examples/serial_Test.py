# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:54:58 2024

@author: EBFoundry
"""

import serial
import time


com = 'COM5'

ser = serial.Serial(com,115200)

while True:
    ser.write(b'0')
    time.sleep(3)
    ser.write(b'1')
    time.sleep(1)
