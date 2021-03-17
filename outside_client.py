import paho.mqtt.client as mqtt
import time

host = "127.0.0.1"
port=8000
clientID = "py" + str(time.time())

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)

def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    print("message received:", payload)
    if (payload == "hello"):
        client.publish("home", "hey there")

client = mqtt.Client(clientID, transport="websockets")
client.on_connect = on_connect 
client.on_message = on_message  
client.connect(host, port=port)
client.subscribe("home")
client.loop_forever()