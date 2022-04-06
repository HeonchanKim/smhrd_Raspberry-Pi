import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
p = gpio.PWM(18,500)
p.start(10)


song = [ 392, 392, 440, 440, 392, 392, 329, 392, 392, 329, 329, 294, 392, 392, 440, 440, 392, 392, 329, 392, 329, 294, 329, 261 ]

list = [261,293,329,349,391,440,493]

#while True:
    #p.ChangeFrequency(262)
    #time.sleep(0.5)
    
for i in song:
    p.ChangeFrequency(i)
    time.sleep(0.5)
    