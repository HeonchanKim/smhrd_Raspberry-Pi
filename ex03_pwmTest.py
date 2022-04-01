import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
gpio.setup(20,gpio.IN)
p = gpio.PWM(18,500)
p.start(0)
cnt = 0


while True:
    btn1 = gpio.input(20)
    if btn1 == 1:
        cnt += 1
        time.sleep(0.1)
        
        if cnt % 3 == 1:
            p.ChangeDutyCycle(30)
            time.sleep(0.1)
        elif cnt % 3 == 2:
            p.ChangeDutyCycle(50)
            time.sleep(0.1)
        elif cnt % 3 == 0:
            p.ChangeDutyCycle(100)
            time.sleep(0.1)

