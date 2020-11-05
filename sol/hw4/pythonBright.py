#!/usr/bin/python3
# A small Python program to set up GPIO4 as an LED that can be
# turned on or off from the Linux console. 
# Written by Derek Molloy for the book "Exploring Raspberry Pi"

import sys
from time import sleep
LED4_PATH = "/sys/class/gpio/gpio4/"
SYSFS_DIR = "/sys/class/gpio/"
LED_NUMBER = "4"
delayTime = 0

def writeLED ( filename, value, path=LED4_PATH ):
   "This function writes the value passed to the file in the path"
   fo = open( path + filename,"w")  
   fo.write(value)
   fo.close()
   return

def closeLED ( filename, path=LED4_PATH):
    "close LED in a procedure method"
    cycle = 0.01
    fo = open( path + filename, "w")
    num = 100
    for d in range(num,0,-1):
        duty = float(d)/num
        dutyTime = cycle * duty
        undutyTime = cycle * (1 - duty)
        for i in range(10):
            writeLED(filename, "1")
            sleep(dutyTime)
            writeLED(filename, "0")
            sleep(undutyTime)
    return
    
print("Starting the GPIO LED4 Python script")
while True:
    command = input("Enter a command of setup, on, off, status, close or quit:")
    try:
        if command == "quit":
            sys.exit(0)
        if command == "on":
            print("Turning the LED on")
            writeLED (filename="value", value="1")
        elif command=="off":
            print("Turning the LED off")
            sleep(delayTime)
            closeLED (filename="value")
        elif command=="setup":
            print("Setting up the LED GPIO")
            writeLED (filename="export", value=LED_NUMBER, path=SYSFS_DIR)
            sleep(0.1);
            writeLED (filename="direction", value="out")
            delayTime = int(input("Input delay time:"))
        elif command=="close":
            print("Closing down the LED GPIO")
            writeLED (filename="unexport", value=LED_NUMBER, path=SYSFS_DIR)
        elif command=="status":
            print("Getting the LED state value")
            fo = open( LED4_PATH + "value", "r")
            print(fo.read())
            fo.close()
        else:
            print("Invalid Command!")
    except Exception as e:
        print(repr(e))
        print("try again.")

