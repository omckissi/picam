import RPi.GPIO as GPIO
import time
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

GPIO.output(17, GPIO.HIGH)
time.sleep(5)
GPIO.output(17, GPIO.LOW)
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
#camera.flash_mode = 'on'
mins = time.time() +30

#camera.capture('fopo.jpg')
def record_video():
    print("recording!")
    #filename = os.path.join(destination, dt.datetime.now().strftime(mouseid + trainday + '_%Y-%m-%d_%H.%M.h264'))
    camera.start_preview(fullscreen=False, window = (650, 500, 640, 480))
    camera.start_recording("/home/pi/Desktop/46.h264")
    camera.wait_recording(mins)
    
record_video()

#while time.time() < mins:
    #if GPIO.input(17) == True:
      #  print("hella")
      #  time.sleep(0.01)
    #else:
        #print("dang")
       # time.sleep(0.01)