import picamera as pc
import time

#1초 간격으로 사진 세장 찍기!

camera = pc.PiCamera()
camera.start_preview()
time.sleep(3)

for i in range(3):
    camera.capture(f'image{i}.jpg')
    time.sleep(1)
camera.stop_preview()
camera.close()
