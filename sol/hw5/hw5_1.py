#!/usr/bin/python3
'''
PWM控制信号周期20ms,脉宽0.5ms-2.5ms对应的角度-90到+90度,范围180度(3度左右偏差),当脉宽1.5ms时舵机在中立点(0度)，我们直接用python的GPIO提供的PWM控制。脉宽0.5ms-2.5ms 对应的占空比为2.5% - 12.5% .
'''
import RPi.GPIO as GPIO
import time
import signal
import atexit
atexit.register(GPIO.cleanup) 
servopin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin,50) #50HZ
p.start(0)
time.sleep(2)

while(True):
    for i in range(0,181,10):
        p.ChangeDutyCycle(2.5 + 10*i/180)
        time.sleep(1)                      #等该20ms周期结束
        #p.ChangeDutyCycle(0)                  #归零信号

    for i in range(181,0,-10):
        p.ChangeDutyCycle(2.5 + 10*i/180)
        time.sleep(1)
        #p.ChangeDutyCycle(0)                  #归零信号
