
##*************************************
## This code is Written and tested by
## Author: VIVEK GR
##*************************************

import RPi.GPIO as GPIO
import time
PIR_INPUT_PIN=13
LED_PIN=40
BUZZER_PIN=15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_INPUT_PIN, GPIO.IN)       #Read output from PIR motion sensor
GPIO.setup(LED_PIN, GPIO.OUT)            #LED output pin
GPIO.setup(BUZZER_PIN, GPIO.OUT)         #Buzzer output pin

while True:
       i=GPIO.input(PIR_INPUT_PIN)
       if i==0:                          #When output from motion sensor is LOW
             print "No intruders",i
             GPIO.output(LED_PIN, 0)     #Turn OFF LED
             GPIO.output(BUZZER_PIN, 0)  #Turn Off Buzzer
             
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(LED_PIN, 1)     #Turn OFF LED
             GPIO.output(BUZZER_PIN, 1)  #Turn Off Buzzer
             time.sleep(0.1)
