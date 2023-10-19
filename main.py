print("Started")
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time

import pygsheets
import pandas as pd

list_monday = ["wwwwww", "iiiii", "wasd"]
list_new = []
for elem in list_monday:    
    list_new.append(elem)


def connectToGoogleDrive():
    
    #authorization
    gc = pygsheets.authorize(service_file='/Users/erikrood/desktop/QS_Model/creds.json')

    # Create empty dataframe
    df = pd.DataFrame()

    # Create a column
    df['name'] = ['John', 'Steve', 'Sarah']

    #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    sh = gc.open('PY to Gsheet Test')

    #select the first sheet 
    wks = sh[0]

    #update the first sheet with df, starting at cell B2. 
    wks.set_dataframe(df,(1,1))






print("Searching cam") 
cap = cv2.VideoCapture(0)
#cap.set(3,640)
#cap.set(4,480)
cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 100)  # brightness


print("Found Cam")
while True:
    ret, frame = cap.read()
    #cv2.imshow('webcam', frame)
    for barcode in decode(frame):
        myData = barcode.data.decode("utf-8")
        inMonday = myData in list_monday
        inListNew = myData in list_new
        if inMonday == True and inListNew == False:
            print(f"Schon eingepackt! {myData}")
        
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