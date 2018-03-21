#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)
LIGHT = 4
GPIO.setup(LIGHT,GPIO.OUT)
while True:
    GPIO.output(LIGHT,True)
    time.sleep(1)
    GPIO.output(LIGHT,False)
    time.sleep(1)
    print("Hello World")
    