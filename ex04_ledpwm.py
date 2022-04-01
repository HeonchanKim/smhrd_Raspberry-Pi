import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
gpio.setup(20,gpio.IN)
p = gpio.PWM(18,500)
p.start(0)
cnt = 0
check = False

try:
    while True:
        btn = gpio.input(20)
        
        if btn == 1:
            if check == False:
                cnt+=1
                check = True
                print(cnt)
        else:
            check=False
        
        if cnt % 3 == 0 :
            p.ChangeDutyCycle(100)
        if cnt % 3 == 1 :
            p.ChangeDutyCycle(30)
        if cnt % 3 == 2 :
            p.ChangeDutyCycle(50)
except KeyboardInterrupt: #ctrl + c
    gpio.cleanup()  
        
        
        
        
        