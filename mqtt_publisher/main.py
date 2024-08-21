import paho.mqtt.client as paho
import paho.mqtt as mqtt
import time

def on_publish(client, userdata, mid):
    print("mid: " + str(mid))

def start() -> None:
    print("Testing HiveMQ MQTT publisher")

    client = paho.Client(client_id="sharizan_redzuan", userdata=None, protocol=paho.MQTTv5)
    # client.tls_set(mqtt.client.ssl.PROTOCOL_TLS)
    #client.connect("ssl://localhost", port=1883)
    # client.connect("ssl://localhost", port=1883)
    # client.username_pw_set("admin","hivemq")
    
    # client.will_set(topic="Test MQTT", payload="Testing message", qos=0, retain=True)
    client.on_publish = on_publish
    client.connect("localhost", port=1883, keepalive=60, clean_start=0)
    client.loop_start()
    
    # client.loop_forever()
    
    # print(client.is_connected())
    # print(connect_status)
    
    temperature = 100
    
    while True:
        temperature = temperature + 1
        (rc, mid) = client.publish("encyclopedia/temperature", str(temperature), qos=2, retain=False)
        # client.will_set(topic="encyclopedia/temperature", payload=None, qos=0, retain=False)
        time.sleep(1)