import mqtt
from network import WLAN
import machine
import time
import abdTest

prKeyAddress = 28418
pbKeyAddress = 28419
cerAddress = 28417

wifi_ssid = "SSID"
wifi_pass = "PASSWORD"

abdTest.readCer(cerAddress)
time.sleep(1)
abdTest.readCer(prKeyAddress)
time.sleep(1)
AWS_CLIENT_CERT = '/flash/cert/certificateMS.pem.crt'
#AWS_ROOT_CA = '/flash/cert/AmazonRootCA3MS.pem'
AWS_PRIVATE_KEY = '/flash/cert/privateMS.pem.key'

def sub_cb(topic, msg):
   print(msg)

wlan = WLAN(mode=WLAN.STA)
wlan.connect(wifi_ssid, auth=(WLAN.WPA2, wifi_pass), timeout=10000)
while not wlan.isconnected():
    machine.idle()
print("Connected to WiFi\n")
time.sleep(1)
AWS_Port = 8883
AWS_URL = "a2ezy2sb17mjr3-ats.iot.eu-central-1.amazonaws.com"
clientID = "PYCOM_GPY_3"
topicPb = "$aws/things/tealcomtest1/shadow/update"
topicSb= "$aws/things/tealcomtest1/shadow/update/accepted"
topic = "thing/RaspberryPi1"


client = mqtt.MQTTClient("PYCOMGPY3",
                    "a2ezy2sb17mjr3-ats.iot.eu-central-1.amazonaws.com",
                    port=8883,
                    keepalive=10000,
                    ssl=True,
                    ssl_params={
                    "certfile":AWS_CLIENT_CERT,
                    "keyfile":AWS_PRIVATE_KEY
                    #"ca_certs":AWS_ROOT_CA,
                    #"server_side"=False
                    })
time.sleep(2)
client.set_callback(sub_cb)

#client.subscribe(topic=topic)
client.connect()
client.subscribe(topic=topicSb)
while True:
    print("Sending ON")
    client.publish(topic=topicPb, msg='{"state":{"reported":{"msg": "hello world from Pycom Board"}}}', qos = 0)
    print("Sent")
    time.sleep(5)
    client.check_msg()
    time.sleep(1)
