import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.OUT)
gpio.setup(20,gpio.IN)
gpio.setup(21,gpio.IN)
try:
    while True:
        btn1 = gpio.input(20)
        btn2 = gpio.input(21)
        print(btn1)
        print(btn2)
        if btn1 == 1:
            gpio.output(16,gpio.HIGH)
        else:
            gpio.output(16,gpio.LOW)
        
        if btn2 == 1:
            gpio.output(18,gpio.HIGH)
        else:
            gpio.output(18,gpio.LOW)
except KeyboardInterrupt: #ctrl + c
    gpio.cleanup()
    
    
    
    
    
    
    
    
    
    
    
    