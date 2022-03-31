import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
p = gpio.PWM(18,500)
p.start(0)

# led 밝기를 0~100까지지 점점 밝아졌다가 다시 점점 어두워지는 프로그램
try:
    while True:
        for i in range(0,200):
            if i <= 100:
                p.ChangeDutyCycle(i)
                time.sleep(0.05)
            else :
                p.ChangeDutyCycle(200-i)
                time.sleep(0.05)
except KeyboardInterrupt: #ctrl + c
    gpio.cleanup()          
      
