import paho.mqtt.client as mqtt #import the client1
import json
import os  
import glob  
import time
import paho.mqtt.client as mqtt #import the client1
import json
broker_address="172.17.0.2"

os.system('modprobe w1-gpio')  
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'  
device_folder = glob.glob(base_dir + '28*')[0]  
device_file = device_folder + '/w1_slave'
#broker_address="iot.eclipse.org" #use external broker
client1 = mqtt.Client("client1") #create new instance
#client2 = mqtt.Client("client2")
client1.connect(broker_address) #connect to broker
print("Connecting to Broker 172.17.0.2")
# đọc dữ liệu nhiệt độ từ file 
#data1 = 'true,2'
def read_temp_raw():  
    f = open(device_file, 'r')  
    lines = f.readlines()  
    f.close()  
    return lines

def read_temp():  
    lines = read_temp_raw()  
    while lines[0].strip()[-3:] != 'YES':  
        time.sleep(0.2)  
        lines = read_temp_raw()  
    equals_pos = lines[1].find('t=')  
    if equals_pos != -1:  
        temp_string = lines[1][equals_pos+2:]  
        temp_c = float(temp_string) / 1000.0  
        temp_f = temp_c * 9.0 / 5.0 + 32.0  
        return temp_c
while True:  
    print(read_temp())      
   # time.sleep(1)
    data1 = read_temp()
    client1.publish("office/sensor1", data1)
    print("pub data to office/sensor1")
    time.sleep(5)