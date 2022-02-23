import RPi.GPIO as GPIO
import time
import datetime as dt
import os
from picamera import PiCamera


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

camera = PiCamera()
#res is length x width
camera.resolution = (1280, 960)
camera.framerate = 30

#filename and save location
mouseid= input('input mouse id: ') +'_'
trainday= input('input training day: ')
destination = '/home/pi/Desktop'

#mins is num of desired minutes
minutes = 30
mins = minutes*60


def record_video():
    print("recording!")
    filename = os.path.join(destination, dt.datetime.now().strftime(mouseid + trainday + '_%Y-%m-%d_%H.%M.h264'))
    camera.start_preview(fullscreen=False, window = (500, 300, 640, 480))
    camera.start_recording(filename)
    camera.wait_recording(mins)

def finish_video():
    camera.stop_recording()
    camera.stop_preview()
    

while True:
    
    if GPIO.input(4)== True:
        record_video()
        finish_video()
        print ("done binch")
        break
    else:
        time.sleep(0.5)
GPIO.cleanup()

#mins = time.time() +15

#while time.time() < mins:
    #if GPIO.input(4) == True:
        #print("hella")
        #time.sleep(0.5)
    #else:
        #print("dang")
        #time.sleep(0.5)FW