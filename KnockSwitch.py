#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt #import the client1
import json
import os  
import glob  
import time
import paho.mqtt.client as mqtt #import the client1
import json
broker_address="172.17.0.2"
client1 = mqtt.Client("client1") #create new instance
#client2 = mqtt.Client("client2")
client1.connect(broker_address) #connect to broker
print("Connecting to Broker 172.17.0.2")
theNumberOfPeople = 0



colors = [0xFF00, 0x00FF, 0x0FF0, 0xF00F]
pins = {'pin_R':15, 'pin_G':16}  # pins is a dict
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in pins:
	   GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
	   GPIO.output(pins[i], GPIO.HIGH)
p_R = GPIO.PWM(pins['pin_R'], 5)  # tan so xung
p_G = GPIO.PWM(pins['pin_G'], 5)  
p_R.start(0)      # Initial duty Cycle = 0(leds on)
p_G.start(0)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col):   # For example : col = 0x112233
	R_val = (col & 0x1100) >> 8
	G_val = (col & 0x0011) >> 0
	
	R_val = map(R_val, 0, 255, 0, 244)
	G_val = map(G_val, 0, 255, 0, 244)
	
	p_R.ChangeDutyCycle(R_val)     # Change duty cycle
	p_G.ChangeDutyCycle(G_val)

	




KnockPin = 11 


#Led_status = 1

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
#	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(KnockPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def swLed(ev=None):
#	global Led_status
#	Led_status = not Led_status
#	GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)
    print "Having motion !!!!"

    for col in colors:
	  setColor(col)
	 # time.sleep(2)
    for i in pins:
	  GPIO.output(pins[i], GPIO.HIGH)
    theNumberOfPeople = theNumberOfPeople + 1


def loop():
	GPIO.add_event_detect(KnockPin, GPIO.FALLING, callback=swLed, bouncetime=200) # wait for falling
	while True:
		pass   # Don't do anything

def destroy():
    GPIO.cleanup()                     # Release resource

#if __name__ == '__main__':     # Program start from here
#	setup()
#	try:
#		loop()
#	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
#		destroy()

while True:  
    #print(theNumberOfPeople)      
   # time.sleep(1)
    if __name__ == '__main__':     # Program start from here
	     setup()
	     try:
		     loop()
	     except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		     destroy()
    print(theNumberOfPeople)
    client1.publish("office/sensor3", theNumberOfPeople)
    print("pub data to office/sensor3")
    #time.sleep(5)
