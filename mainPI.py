# Credit: Adrian Rosebrock
# https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
 
# import the necessary packages
#from picamera.array import PiRGBArray # Generates a 3D RGB array
from picamera2 import Picamera2
from libcamera import Transform

import numpy as np
from pyzbar.pyzbar import decode
import time # Provides time-related functions
import cv2 # OpenCV library


list_monday = ["wwwwww", "iiiii", "wasd"]
list_new = []
for elem in list_monday:    
    list_new.append(elem)


picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(transform=Transform(hflip=True))
#raw_capture = PiRGBArray(camera, size=(640, 480))
 
# Wait a certain number of seconds to allow the camera time to warmup
time.sleep(0.1)
 
# Capture frames continuously from the camera
for frame in picam2.capture_continuous(picam2, format="bgr", use_video_port=True):
     
    # Grab the raw NumPy array representing the image
    image = frame.array

    cv2.imshow("Frame", image)

    for barcode in decode(frame):
        myData = barcode.data.decode("utf-8")
        inMonday = myData in list_monday
        inListNew = myData in list_new
        if inMonday == True and inListNew == False:
            print("Schon eingepackt!")
        
        for elem in list_new:
            if elem == myData and myData in list_monday:
                list_new.remove(elem)
                print("Fertig")

    key = cv2.waitKey(1) & 0xFF
     
    raw_capture.truncate(0)

    if key == ord("q"):
        break