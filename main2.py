from mqtt import MQTTClient
from network import WLAN
import machine
import time
import binascii
import abdTest

#AWS_ROOT_CA = '/flash/cert/AmazonRootCA3.pem'
AWS_CLIENT_CERT = '/flash/cert/certificate.pem.crt'
AWS_PRIVATE_KEY = '/flash/cert/private.pem.key'

def sub_cb(topic, msg):
   print(msg)
prKeyAddress = 28418
pbKeyAddress = 28419
cerAddress = 28417
wifi_ssid = "YOUR_NETWORK_SSID"
wifi_pass = "YOUR_NETWORK_PASSWORD"

wlan = WLAN(mode=WLAN.STA)
wlan.connect(wifi_ssid, auth=(WLAN.WPA2, wifi_pass), timeout=5000)
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
#caCer = abdTest.readCer(cerAddress)
#prKey = abdTest.readCer(prKeyAddress)
#print(binascii.unhexlify(prKey))
#pbKey = abdTest.readCer(pbKeyAddress)

#                    "a2ezy2sb17mjr3-ats.iot.eu-central-1.amazonaws.com",
#                    "cert":binascii.unhexlify(caCer),
#                    "key":binascii.unhexlify(prKey),
#                    "server_side":False
client = MQTTClient(clientID,
                    AWS_URL,
                    port=AWS_Port,
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
client.connect()
client.subscribe(topic=topic)
while True:
    print("Sending ON")
    client.publish(topic=topic, msg='{"state":{"reported":{"msg": "hello world from Pycom Board"}}}', qos = 0)
    print("Sent")
    time.sleep(5)
    client.check_msg()
    time.sleep(1)
