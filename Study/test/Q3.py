import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
gpio.setup(20,gpio.IN)
gpio.setup(21,gpio.IN)
p = gpio.PWM(18,500)
p.start(0)
cnt = 0

try:
    while True:
        btn1 = gpio.input(20)
        btn2 = gpio.input(21)
        if btn1 == 1:
            p.ChangeDutyCycle(50)
        
        if btn2 == 1:
            p.ChangeDutyCycle(100)
except KeyboardInterrupt: #ctrl + c
    gpio.cleanup()
    
