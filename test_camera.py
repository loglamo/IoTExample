

import paho.mqtt.client as mqtt #import the client1
import json
import os  
import glob  
import time
import paho.mqtt.client as mqtt #import the client1
import json




#address of broker 
broker_address="172.17.0.1"

#os.system('modprobe w1-gpio')  
#os.system('modprobe w1-therm')


#broker_address="iot.eclipse.org" #use external broker
client1 = mqtt.Client("client1") #create new instance
client1.connect(broker_address)
print("Connecting to Broker 172.17.0.1")

per = 1

if(per == 1):  # have sbd out door 
    f=open("./test1.jpg", "rb") 
    fileContent = f.read()
    byteArr = bytearray(fileContent)
    client1.publish("office/my-image", byteArr)# send image to HA
    client1.publish("office/alarm", "disarmed")# send Alarm to HA 
    print("pub data to office/my-camera")
    print("teeeeeee.....")
    time.sleep(15)# wait 3s 
    
   
else:
    fn = open("./user.jpg", "rb")
    fileContent_fn = fn.read()
    byteArr_fn = bytearray(fileContent_fn)
    client1.publish("office/my-image", byteArr_fn)
    client1.publish("office/alarm", "armed_home")
    print("Nobody here ")
    time.sleep(15)
fn = open("./user.jpg", "rb")
fileContent_fn = fn.read()
byteArr_fn = bytearray(fileContent_fn)
client1.publish("office/my-image", byteArr_fn)
client1.publish("office/alarm", "armed_home")
print("Nobody here ")