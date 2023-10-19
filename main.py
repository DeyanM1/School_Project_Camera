print("Started")
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time


list_monday = ["wwwwww", "iiiii", "wasd"]
list_new = []
for elem in list_monday:    
    list_new.append(elem)


print("Searching cam") 
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

print("Found Cam")
while True:
    ret, frame = cap.read()
    cv2.imshow('webcam', frame)
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


                
        
        time.sleep(3)
        #print(myData, list_new)
        #print(myData in list_monday, myData in list_new)



    #cv2.imshow("In",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break