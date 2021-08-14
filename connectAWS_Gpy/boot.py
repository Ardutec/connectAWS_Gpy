from network import WLAN
import machine
wifi_ssid = "InvoTech"
wifi_pass = "idontknow"
#wifi_ssid = "Nextera"
#wifi_pass = "#@nes2021"
wlan = WLAN(mode=WLAN.STA)
wlan.connect(wifi_ssid, auth=(WLAN.WPA2, wifi_pass), timeout=5000)
while not wlan.isconnected():
    machine.idle()
