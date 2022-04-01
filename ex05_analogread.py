import spidevRead as sr
import time
import RPi.GPIO as gpio
import led18

while True:
    readData = sr.analog_read(0)
    print(readData)
    
    if readData < 900:
        led18.ledon()
    else :
        led18.ledoff()