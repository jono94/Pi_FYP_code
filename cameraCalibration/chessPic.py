
from picamera import PiCamera
import cv2
import numpy as np
import time
camera = PiCamera()
camera.resolution = (680,480)
camera.start_preview()
for i in range(0,40):
    print '2'
    time.sleep(1)
    print '1'
    time.sleep(1)
    print 'Image Taken'
    camera.capture('images/Chess'+str(time.time())+'Res680480.jpg')

