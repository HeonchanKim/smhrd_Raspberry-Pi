import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)

def ledon():
    gpio.output(18,gpio.HIGH)

def ledoff():
    gpio.output(18,gpio.LOW)
