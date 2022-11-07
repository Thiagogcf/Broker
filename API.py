import datetime
import random

from Data import Teste


import random
import time

from paho.mqtt import client as mqtt_client

broker = '191.233.31.141'
port = 1883
topic = "TESTE"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# python3.6
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        t1 = Teste(
            dado=(msg.payload.decode())+" "+str(datetime.datetime.now())
        )

        t1.save()

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
