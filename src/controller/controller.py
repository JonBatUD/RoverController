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

import keyboard
import threading


keyboard.add_hotkey('space', lambda: print('space was pressed!'))
# Detect key press

running = False

HOST = '192.168.1.143'
PORT = 5555



class sender():
    def __init__(self,HOST,PORT):
        self.conection = self.connect(HOST,PORT)
        self.run()

    def connect(self, HOST,PORT):
        soc =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((HOST,PORT))

        return soc
    
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST,PORT))
            
            while True:
                try:
                    # Get a keqqy press
                    # Send the coresponding byte
                    #s.send(b'1')
                    #msg = s.recv(3)
                    #print(msg)
                    time.sleep(.1)
                    if keyboard.is_pressed('q'):
                        self.conection.send(b'1')
                        print('q pressed')

                    if keyboard.is_pressed('a'):
                        self.conection.send(b'2')
                        print('a pressed')

                    if keyboard.is_pressed('e'):
                        self.conection.send(b'4')
                        print('e pressed')
                
                    if keyboard.is_pressed('d'):
                        self.conection.send(b'5')
                        print('d pressed')
                
                    if keyboard.is_pressed('esc'):
                        self.conection.send(b'0')
                        print('esc pressed')

                except KeyboardInterrupt:
                    self.conection.send(b'0')
                    self.conection.close()
                    
    def close():
        self.sendStop()
        self.connection.close()


    def sendStop(self):
        self.connection.send(b'0')




if __name__ == '__main__':
    
    active_sender = sender(HOST,PORT)
    