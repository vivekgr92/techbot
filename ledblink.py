##*************************************
## This code is Written and tested by
## Author: VIVEK GR
##************************************* 
import RPi.GPIO as GPIO 
import time 
PIN_NO=12
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 
GPIO.setup(PIN_NO, GPIO.OUT) 
for x in xrange(500):
	GPIO.output(PIN_NO,GPIO.HIGH) 
	time.sleep(2)
	GPIO.output(PIN_NO,GPIO.LOW ) 
	time.sleep(2) 
GPIO.cleanup() 
