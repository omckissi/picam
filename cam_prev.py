from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (640, 480)


camera.start_recording('mw07d6.h264')
camera.wait_recording(60*20)
camera.stop_recording()
