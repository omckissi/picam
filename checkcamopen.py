import RPi.GPIO as GPIO
import time
import datetime as dt
import os
from picamera import PiCamera


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

print(camera._check_camera_open())