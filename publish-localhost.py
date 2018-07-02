# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.connect("localhost", 1883)
mqttc.publish("Topico/Lampada", "Ligar")
mqttc.loop(2)
