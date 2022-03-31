import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
#gpio.output(18,gpio.HIGH)
#gpio.output(18,gpio.LOW)
#time.sleep(5)

try:
    while True:
        gpio.output(18,gpio.HIGH)
        time.sleep(0.5)
        gpio.output(18,gpio.LOW)
        time.sleep(0.5)
except KeyboardInterrupt: #ctrl + c
    gpio.cleanup()