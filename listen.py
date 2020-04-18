#!/usr/bin/env python3
import faulthandler; faulthandler.enable()
import sys, signal
import time
import datetime
import crc16

from rf95 import RF95, Bw31_25Cr48Sf512

def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    rf95.set_mode_idle()
    rf95.cleanup()
    sys.exit(0)
    
def reset_RF95():
    global rf95
    global numberofReset
    print("RF95 Reset")
    numberofReset +=1
    rf95.set_mode_idle()
    rf95.cleanup()
    rf95.init()
    return time.time()
    pass

"""
char* encryptDecrypt(char *toEncrypt,uint8_t sizeData) 
{
    char key[8] = {'1', 'q', '2','w','3','e','4','r'}; //Any chars will work
    char* output = toEncrypt;
    int i =0;
    for (i = 0; i < sizeData; i++)
        output[i] = toEncrypt[i] ^ key[i % (sizeof(key) / sizeof(char))];
    return output;
}
"""
def encryptDecrypt(_data,datalen):
  key = ('1', 'q', '2','w','3','e','4','r')
  
  #print("\nKEY type", type(key))
 
  i=0
  #print(key[int(i % (len(key)/8))])

  output=_data
  while datalen > i:
    keyValue = ord(key[int(i % len(key))])
    output[i]=_data[i] ^ keyValue
    i +=1

  return output



if __name__ == "__main__":
    rf95 = RF95(0, int_pin=25, reset_pin=22, address=100,promiscuousMode=True)
    rf95.set_frequency(437)
    rf95.set_tx_power(23)
    lastReceived = time.time()
    numberofReset=0
    print(rf95.promiscuousMode)
    
    if not rf95.init():
        print("RF95 not found")
        rf95.cleanup()
        quit(1)
    else:
        print("RF95 LoRa mode ok")

    
    resetFlag = False
    counter = 0
    while True:    
      while not rf95.available():
        signal.signal(signal.SIGINT, signal_handler)
        if time.time()-lastReceived > 10:
          lastReceived = reset_RF95()
          resetFlag = True
          break
        pass
      

      if not resetFlag: 
        data = rf95.recv()
        data.pop()
        print("got Data from ",rf95.rxHeaderFrom,"size = ", len(data)," | data = ",end="")
        decypt = encryptDecrypt(data,len(data))
        for i in decypt:
          print(chr(i), end="")
        
        
        timeVar=datetime.datetime.now()
        print("| @",timeVar.strftime("%X")," - CRC ", hex(crc16.crc16xmodem(bytes(data))))
        

        lastReceived = time.time()
     
      resetFlag = False
      pass
