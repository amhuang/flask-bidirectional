import paho.mqtt.client as mqtt
import time

host = "localhost"
port = 8000
clientID = "pyclient" + str(time.time())

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)

def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    print("message received:", payload)
    if (payload == "hello"):
        client.publish("home", "hi there!")

client = mqtt.Client(clientID, transport="websockets")
client.on_connect = on_connect 
client.on_message = on_message  
client.connect(host, port=port)
client.subscribe("jsresponse")

while True:
    client.loop_start()
    client.publish("home", "hi from " + clientID)
    print("message sent")
    time.sleep(5)
    client.loop_stop()