import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connecting with" + str(rc))
    client.subscribe("paho/temperature")

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass


client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish


client.connect("localhost", 1883)

temp = 0

while True:
    temp = temp +1
    temperature = temp
    client.publish("paho/temperature", temperature)
    time.sleep(1)