##*************************************
## This code is Written and tested by
## Author: VIVEK GR
##************************************* 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)  # Same label as T cobbler kit 
TRIG=23                 # #23 in Tcobbler 
ECHO=24                 # #24 in Tcobbler

print "Distance Measurement-Ongoing Please Wait...."

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,False)
print "Waiting For Sensor to Settle"
time.sleep(2)

GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False)

while GPIO.input(ECHO)==0:
    pulse_start=time.time()

while GPIO.input(ECHO)==1:
    pulse_end=time.time()

pulse_duration=pulse_end - pulse_start
distance=pulse_duration *17150
distance=round(distance,2)
print "Distance:",distance,"cm"

GPIO.cleanup()
