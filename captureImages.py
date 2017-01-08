
import time
import picamera
import glob
import shutil
import os

image_path = 'stream_image_set/images/'
fps = 10
res = (640,480)
runTime = 220

#allow sendImages to remove all images if they exist
time.sleep(1)
#start up camera and take images
with picamera.PiCamera() as camera:

    camera.resolution = res
    camera.framerate = fps

    #camera.shutter_speed = camera.exposure_speed
    #camera.exposure_mode = 'off'

    #g = camera.awb_gains
    #camera.awb_mode = 'off'
    #camera.awb_gains = g

    if False:
        i = 5
        print '\nStart Recording in:'
        while i>0:
            print i
            time.sleep(1)
        print '****Recording****'

    camera.start_preview()
    # here we go
    try:
        for filename, i in enumerate(camera.capture_continuous(image_path+'{timestamp:%H_%M_%S_%f}_{counter:08d}.jpg',use_video_port=True)):
            checkState = open('state.txt','rb')
            state      = ''
            for line in checkState:
                state = line
            checkState.close()
            if (state=='pause')or(state=='exit'): #stop image taking
                break
    finally:
        camera.stop_preview()
