import paho.mqtt.client as mqtt
import json
import time

def send_new_data(client_id, token, secret, data,topic):
    client = mqtt.Client(client_id=client_id)
    client.username_pw_set(username=token, password=secret)
    client.connect(host="localhost", port=1883, keepalive=60)
    time.sleep(0.5)
    new_dict = dict()
    new_dict["data"] = data
    payload = json.dumps(new_dict)
    client.publish(topic, payload=payload)
    client.disconnect()

data = {
    "temperature": 25,
    'o2': 98,
    "heartrate": 89,
    "timestamp":'CURRENT_TIME'
    }

if __name__ == "__main__":
    send_new_data("1",
                "mqtt",
                "password",
                data,
                "homeIsolation"
                )