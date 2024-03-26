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

keyboard.add_hotkey('space', lambda: print('space was pressed!'))
# Detect key press
while True:
    
    try:
        if keyboard.is_pressed('q'):
            print('q pressed')

        if keyboard.is_pressed('a'):
            print('a pressed')

        if keyboard.is_pressed('e'):
            print('e pressed')
    
        if keyboard.is_pressed('d'):
            print('d pressed')
    
        if keyboard.is_pressed('esc'):
            print('esc pressed')
    except:
      
        break
        