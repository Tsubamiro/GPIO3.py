import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GIPO.setup(15,GIPO.OUT)
GIPO.setup(2,GPIO.IN)

try:
    while True:
        if GPIO.input(2) == GPIO.LOW:
            GPIO.output(15,GPIO.HIGH)
        else:
            GPIO.output(15,GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()