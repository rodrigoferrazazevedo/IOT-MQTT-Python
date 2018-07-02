# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.username_pw_set("rcjwrmig","luNqlsda3Ma_")
mqttc.connect("m13.cloudmqtt.com", 12389, 60)
mqttc.publish("Topico/Lampada", "Ligar")
mqttc.loop(2)
