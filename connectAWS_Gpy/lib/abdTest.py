import machine
import binascii
from network import LTE
prKeyAddress = 28418
pbKeyAddress = 28419
cerAddress = 28417
chunLen = 255
lte = LTE()
def readCer(address):
    reply = lte.send_at_cmd("AT+CRSM=176,"+str(address)+",0,0,2,,\"3F007F70\"")
    #reply1 = reply.decode("utf-8")
    #print(reply)
    start = reply.find("144,0,")
    sLen = reply[start+6:start+10]
    #print(sLen)
    iLen = int(sLen, 16)
    #print(iLen)
    #reply = lte.send_at_cmd("AT+CRSM=176,"+str(address)+",0,0,"+str(chunLen)+",,\"3F007F70\"")
    #print(reply)
    #tempBuff = reply[start+10:chunLen*2]
    #print(tempBuff)
    p1 = 0
    p2 = 2
    pNot = p2
    tempBuff = ""
    for x in range((iLen/chunLen)+1):
        reply = lte.send_at_cmd("AT+CRSM=176,"+str(address)+","+str(p1)+","+str(p2)+","+str(chunLen)+",,\"3F007F70\"")
        #print(reply)
        start=reply.find("144,0,")
        end = reply.find("FF")

        if(end != -1):
            tempBuff += reply[start+6:end]
            break
        tempBuff += reply[start+6:start+(6+(chunLen*2))]
        pNot += chunLen
        p1 = pNot
        p1 >>= 8
        #print(p1)
        #print(pNot)
    # print(type(tempBuff))
    # return tempBuff
    if(address == cerAddress):
        AWS_CLIENT_CERT1 = "-----BEGIN CERTIFICATE-----\n"
        AWS_CLIENT_CERT1 += binascii.unhexlify(tempBuff).decode('utf-8')
        AWS_CLIENT_CERT1 += "\n-----END CERTIFICATE-----"
        file = open('/flash/cert/certificateMS.pem.crt', "w")
        file.write(AWS_CLIENT_CERT1)
        file.close()
    elif(address == prKeyAddress):
        AWS_PRIVATE_KEY1 = "-----BEGIN RSA PRIVATE KEY-----\n"
        AWS_PRIVATE_KEY1 += binascii.unhexlify(tempBuff).decode('utf-8')
        AWS_PRIVATE_KEY1 += "\n-----END RSA PRIVATE KEY-----"
        file1 = open("/flash/cert/privateMS.pem.key", "w")
        file1.write(AWS_PRIVATE_KEY1)
        file1.close()
#caCer = readCer(cerAddress)
#print(binascii.unhexlify(caCer))
