# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:54:21 2024

@author: EBFoundry

RPi contoller 

Control a motor
Flow
    User input Keyboard
    Server to Rpi
    Rpi client
    Rpi serial print line
    Arduino Serial read 
    Arduino Function controll motor


Arduino 
Serial 
Rpi 


Goal Control a motor through 
User can control the motor 
Create a server 
"""

import keyboard

# Detect key press
while True:
    
    try:
        if keyboard.is_pressed('q'):
            print('q pressed')
    except:
        break
        