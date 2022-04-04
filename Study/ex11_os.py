#os -> operating system
import os
import time
os.system('ifconfig')

#동영상 촬영!
#mp4파일로 변경! -> MP4Box -add ___.h264 ___.mp4

os.system('raspivid -o test4.h264')
time.sleep(6)
os.system('MP4Box -add test4.h264 test4.mp4')




