import machine
#import binascii
from network import LTE
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
    return tempBuff
#caCer = readCer(cerAddress)
#print(binascii.unhexlify(caCer))
