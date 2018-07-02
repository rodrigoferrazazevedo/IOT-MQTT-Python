# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

def on_connect(self, client, userdata, rc):
    print("Connected with result code "+str(rc))
    self.subscribe("Topico/Lampada", 0)

def on_message(client, userdata, msg):
    print("Topic: "+ msg.topic + "Message: "+str(msg.payload))
    if msg.payload == "Ligar":
        print("Lampada ligada!")


#def on_connect(self, mosq, obj, rc):
#        self.subscribe("hello/world", 0)


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost") #test.mosquitto.org

client.loop_forever()
