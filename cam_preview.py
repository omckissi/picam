from picamera import PiCamera
import time
#import RPi.GPIO as GPIO

camera = PiCamera()
camera.resolution = (1280,960)
camera.rotation = 180
#camera.preview_window=(0,0, 400,533)

camera.start_preview(fullscreen=False, window = (500, 300, 640,480))
time.sleep(30)
camera.stop_preview()