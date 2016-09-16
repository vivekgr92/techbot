#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy bly
# 
#************************************************************************
import spidev
import time
import os

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
import spidev
import time
 
spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
# read SPI data from MCP3208 chip, 8 possible adc's (0 thru 7)
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout
 
while True:
    value = readadc(0)
    value1=readadc(1)
    
    volts = (value * 3.3) / 4096
    temperature = volts / (10.0 / 1000)
    print ("%4d/1023 => %5.3f V => %4.1f °C" % (value, volts,
            temperature))
   
   Vout=value1*(3.3/4096)
   print("%4.1f" %(Vout))
   RLDR=(10000.0*(3.3-Vout))
   Lux=(500.0/RLDR)
   print("\n*************************LUX*****************************")
   print("Lux Value %4.1f" %(Lux))
   time.sleep(0.5)
