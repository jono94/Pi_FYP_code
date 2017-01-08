import os
import paramiko
import thread
import time
from ftplib import FTP, FTP_TLS
import socket

localpath = '/home/pi/src/OpenCV/stream_image_set/images/'
remotepath = '/home/jono/src/ORB_image_folder/streaming_images/'
imagepath = 'stream_image_set/images/'

ftp = FTP('ip','name','password')
ftp.cwd(remotepath)

#remove all old images
all_images = [f for f in os.listdir(imagepath) if os.path.isfile(os.path.join(imagepath,f))]
for f in all_images:
    os.remove(imagepath+f)

def sendImages():
    all_images = [f for f in os.listdir(imagepath) if os.path.isfile(os.path.join(imagepath,f))]
    all_images.sort(key=str.lower)
    if(len(all_images)>1):
        for i in range(len(all_images)-1):
            imageFile = open(localpath+all_images[i],'rb')
            ftp.storbinary('STOR '+all_images[i],imageFile)
            imageFile.close()
            os.remove(localpath+all_images[i])
 
while True:
    sendImages()
    checkState = open('state.txt','rb')
    state = ''
    for line in checkState:
        state = line
    checkState.close()
    if (state=='pause')or(state=='exit'):
        sendImages()
        break


ftp.quit()

