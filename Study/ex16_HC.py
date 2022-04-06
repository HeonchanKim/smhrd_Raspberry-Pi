import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
trig = 23
echo = 24
piezo = 18

gpio.setup(trig, gpio.OUT) #트리거핀을 출력으로 사용
gpio.setup(echo, gpio.IN) #에코핀을 입력으로 사용
gpio.setup(piezo, gpio.OUT)
buzz = gpio.PWM(18,500)
try:
    
    while True:
        gpio.output(trig,gpio.LOW)
        time.sleep(0.5)
        gpio.output(trig,gpio.HIGH)
        time.sleep(0.00001) #기본단위가 1초 -> 10마이크로초
        gpio.output(trig, gpio.LOW)
        while gpio.input(echo) == 0: # 펄스 발생(초음파 전송이 끝나는 시간) pulse_start에 저장
            pulse_start = time.time()
        while gpio.input(echo) == 1: # 펄스 돌아옴(초음파 수신이 완료될때까지 시간) pulse_end에 저장
            pulse_end = time.time()
        pulse_duration = pulse_end-pulse_start #거리 = 시간 * 속력
        distance = pulse_duration * 17000 # 기본 공기 중소리의 속력 = 340ms/s 왕복 속력이기 때문에 나누기 2해줌 s로 단위변경
        distance = round(distance,2)
        
        print(f'distance:{distance}cm') # 거리 출력
        if (distance <= 40 and distance > 25):
            buzz.start(10)
            buzz.ChangeFrequency(523)
            time.sleep(0.3)
            buzz.stop()
            time.sleep(0.3)
        elif(distance <= 25 and distance > 10):
            buzz.start(10)
            buzz.ChangeFrequency(523)
            time.sleep(0.15)
            buzz.stop()
            time.sleep(0.15)
        elif distance <= 10:
            buzz.start(90)
            buzz.ChangeFrequency(523)
            time.sleep(0.05)
            buzz.stop()
            time.sleep(0.05)
        else:
            buzz.stop()
            time.sleep(0.05)
            
except KeyboardInterrupt:
    gpio.cleanup()