# RoverController


## Overview
The purpose of this doc is to lay out how to hack together a remote control for the rover. 

## Flow
The direction of flow will be from the computer to the motors:
Computer/Keyboard → RPi/Server → Arduino/MotorController

The user will press a button on the pc keyboard which will send a byte to the raspberry pi. 
The raspberry pi will receive the byte and forward it to the arduino via serial/usb
The arduino will receive the byte and power the motor (or stop the motor).

## Computer/Keyboard
Purpose:
Get input from keyboard,
Send a byte to Raspberry pi

language : Python

Description: 
	Create a client socket to send key presses as bytes to a Raspberry pi server socket. 
Todo
Map keybindings 
Detect keypress ( InProgress)
Write code to send the byte (InProgress)


## RPi/Server
Purpose:
	Receive a byte from pc,
	Print the byte using serial

language : Python

Description: 
	Create a server socket to receive commands from a computer over wifi. Then send the command over serial usb to  an arduino. 
Todo 
Receive a byte (Done)
Print byte over serial (Done)

## Arduino/MotorController
Purpose:
	Receive a byte from serial. Control the motors according to the byte.

language : C++

Description: 
	Receive a byte over serial usb. Based o

Todo 
Define forward and backward pins for each motor
Map bytes to the correct motor and direction 
Receive a byte from serial (Done)
Send the correct command to the motor

ByteMapping
Purpose:
Define what a key press dose


|Keyboard Button | Action | Byte |
--- | --- |---
Q | Left Motors Forward      | 1
A | Left Motors Backward     | 2
Q | release Left motors stop | 3
A release | Left motors stop | 3
E | Right motors Forward | 4
D | Right motors Backward | 5
E release | Right motors stop | 6
D release | Right motors stop | 6




