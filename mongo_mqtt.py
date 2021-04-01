import os
import pymongo
import paho.mqtt.client as mqtt
import time

host = "localhost"
port = 8000
clientID = "pyclient" + str(time.time())

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected, returned code=",rc)
    else:
        print("Bad connection, returned code=",rc)

client = mqtt.Client(clientID, transport="websockets")
client.on_connect = on_connect 
client.connect(host, port=port)

mongo = pymongo.MongoClient()
with mongo.watch() as stream:
    for change in stream:
        client.loop_start()
        client.publish("home", change['fullDocument']['thing_id'])
        client.loop_stop()
        print(change)