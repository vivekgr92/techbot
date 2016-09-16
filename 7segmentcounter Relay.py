

##*************************************
## This code is Written and tested by
## Author: VIVEK GR
##*************************************

import RPi.GPIO as GPIO 
import time

Pin_a=38
Pin_b=36
Pin_c=33
Pin_d=31
Pin_e=29
Pin_f=32
Pin_g=12
Pin_dp=35

Pin_led=40

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(Pin_a, GPIO.OUT)
GPIO.setup(Pin_b, GPIO.OUT)
GPIO.setup(Pin_c, GPIO.OUT)
GPIO.setup(Pin_d, GPIO.OUT)
GPIO.setup(Pin_e, GPIO.OUT)
GPIO.setup(Pin_f, GPIO.OUT)
GPIO.setup(Pin_g, GPIO.OUT)
GPIO.setup(Pin_dp,GPIO.OUT)
GPIO.setup(Pin_led,GPIO.OUT)

pos=0

for x in xrange(1):
    ## Number 1
    GPIO.output(Pin_f, GPIO.HIGH)
    GPIO.output(Pin_e, GPIO.HIGH)
   
    GPIO.output(Pin_a,GPIO.LOW)
    GPIO.output(Pin_b,GPIO.LOW)
    GPIO.output(Pin_g,GPIO.LOW)
    GPIO.output(Pin_c,GPIO.LOW)
    GPIO.output(Pin_d,GPIO.LOW)
    GPIO.output(Pin_dp,GPIO.LOW)

    time.sleep(1)

    ##Number 2
    
    GPIO.output(Pin_a, GPIO.HIGH)
    GPIO.output(Pin_b, GPIO.HIGH)
    GPIO.output(Pin_g, GPIO.HIGH)
    GPIO.output(Pin_e, GPIO.HIGH)
    GPIO.output(Pin_d, GPIO.HIGH)
   
    GPIO.output(Pin_f,GPIO.LOW)
    GPIO.output(Pin_c,GPIO.LOW)
    GPIO.output(Pin_dp,GPIO.LOW)

    time.sleep(1)


    #Number 3
    GPIO.output(Pin_a, GPIO.HIGH)
    GPIO.output(Pin_b, GPIO.HIGH)
    GPIO.output(Pin_g, GPIO.HIGH)
    GPIO.output(Pin_c, GPIO.HIGH)
    GPIO.output(Pin_d, GPIO.HIGH)
   
    GPIO.output(Pin_f,GPIO.LOW)
    GPIO.output(Pin_e,GPIO.LOW)
    GPIO.output(Pin_dp,GPIO.LOW)

    time.sleep(1)


    #Number 4
    GPIO.output(Pin_f, GPIO.HIGH)
    GPIO.output(Pin_g, GPIO.HIGH)
    GPIO.output(Pin_b, GPIO.HIGH)
    GPIO.output(Pin_c, GPIO.HIGH)
    
   
    GPIO.output(Pin_a,GPIO.LOW)
    GPIO.output(Pin_e,GPIO.LOW)
    GPIO.output(Pin_d,GPIO.LOW)
    GPIO.output(Pin_dp,GPIO.LOW)

    time.sleep(1)


    #Number 5
    
    GPIO.output(Pin_a, GPIO.HIGH)
    GPIO.output(Pin_f, GPIO.HIGH)
    GPIO.output(Pin_g, GPIO.HIGH)
    GPIO.output(Pin_c, GPIO.HIGH)
    GPIO.output(Pin_d, GPIO.HIGH)
   
    GPIO.output(Pin_b,GPIO.LOW)
    GPIO.output(Pin_e,GPIO.LOW)
    GPIO.output(Pin_dp,GPIO.LOW)

    time.sleep(1)


    #Number 6
    GPIO.output(Pin_a, GPIO.HIGH)
    GPIO.output(Pin_f, GPIO.HIGH)
    GPIO.output(Pin_g, GPIO.HIGH)
    GPIO.output(Pin_c, GPIO.HIGH)
    GPIO.output(Pin_d, GPIO.HIGH)
    GPIO.output(Pin_e, GPIO.HIGH)
   
    GPIO.output(Pin_b,GPIO.LOW)
    GPIO.output(Pin_dp,GPIO.LOW)

    time.sleep(1)


    #Number 7

    GPIO.output(Pin_a, GPIO.HIGH)
    GPIO.output(Pin_b, GPIO.HIGH)
    GPIO.output(Pin_c, GPIO.HIGH)

    GPIO.output(Pin_f,GPIO.LOW)
    GPIO.output(Pin_g,GPIO.LOW)
    GPIO.output(Pin_d,GPIO.LOW)
    GPIO.output(Pin_e,GPIO.LOW)
    GPIO.output(Pin_dp,GPIO.LOW)

    time.sleep(1)


    # Number 8
    GPIO.output(Pin_a, GPIO.HIGH)
    GPIO.output(Pin_b, GPIO.HIGH)
    GPIO.output(Pin_c, GPIO.HIGH)
    GPIO.output(Pin_d, GPIO.HIGH)
    GPIO.output(Pin_e, GPIO.HIGH)
    GPIO.output(Pin_f, GPIO.HIGH)
    GPIO.output(Pin_g, GPIO.HIGH)
    GPIO.output(Pin_dp, GPIO.HIGH)

    time.sleep(1)

     # Number 9
    GPIO.output(Pin_a, GPIO.HIGH)
    GPIO.output(Pin_b, GPIO.HIGH)
    GPIO.output(Pin_c, GPIO.HIGH)
    GPIO.output(Pin_d, GPIO.HIGH)
    GPIO.output(Pin_f, GPIO.HIGH)
    GPIO.output(Pin_g, GPIO.HIGH)
    GPIO.output(Pin_dp, GPIO.HIGH)

    GPIO.output(Pin_e, GPIO.LOW)

    time.sleep(1)

    print('Timer Reset')
    GPIO.output(Pin_led, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(Pin_led, GPIO.LOW)
GPIO.cleanup() 
    
    
