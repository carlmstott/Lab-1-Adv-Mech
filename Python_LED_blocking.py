import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
while True:
   GPIO.output(18,GPIO.HIGH)
   print ("LED ON")
   sleep(1)
   GPIO.output(18,GPIO.LOW)
   print ("LED OFF")
   sleep(1)