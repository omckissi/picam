import RPi.GPIO as GPIO
import time
import datetime as dt
import os
from picamera import PiCamera


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

mouseid= input('input mouse id: ') +'_'
trainday= input('input training day: ')
mins =40*60
destination = '/home/pi/Desktop'

def record_video():
    print("recording!")
    filename = os.path.join(destination, dt.datetime.now().strftime(mouseid + trainday + '_%Y-%m-%d_%H.%M.h264'))
    camera.start_preview(fullscreen=False, window = (650, 500, 640, 480))
    camera.start_recording(filename)
    camera.wait_recording(mins)

def finish_video():
    camera.stop_recording()
    camera.stop_preview()
    

while True:
    
    if GPIO.input(4)== True:
        record_video()
        finish_video()
        print ("done")
        break
    else:
        time.sleep(0.1)
GPIO.cleanup()

#mins = time.time() +15

#while time.time() < mins:
    #if GPIO.input(4) == True:
        #print("hella")
        #time.sleep(0.5)
    #else:
        #print("dang")
        #time.sleep(0.5)FW