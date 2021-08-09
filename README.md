# connectAWS_Gpy
This Repository read certificates from eSIM and connect Pycom Gpy board with AWS IoT Core via MQTT, to publish and subcribe data. File at "connectAWS_Gpy/lib/AbdTest.py" is the code to read certificates from eSIM.
 
## Test Scenario
For now this code is tested using external certificates rather than certificate stored on eSIM. 

## How to Guide
Download the repository with commad:

> git clone https://github.com/Ardutec/connectAWS_Gpy

Extract "connectAWS_Gpy" folder and save at "Atom" installed directory. In most cases that would be at "C:\Users\user_name\.atom\"

Extract your certificates and save them in cert folder. Name device certificate as "certificate.pem.crt" and private key as "private.pem.key"

Just in case you chose different directory and names, update certificates address in main2.py file. 
Also update "wifi_ssid", "wifi_pass" and "AWS_URL" in main2.py

Go the "settings" file and write "connectAWS_Gpy" at the space for "sync folder"

Upload the folder, it will take some time. Then run main2.py file. 
