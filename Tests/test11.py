print("start")
import cv2
import numpy as np
import time
print("import finish")

print("cap")
cap = cv2.VideoCapture(0)  # Use 0 to access the default camera
cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 100)  # brightness

print(cap.isOpened())

print(cap)

print("while True")
while True:

    print("ret")
    ret, frame = cap.read()
    print(ret, frame)
    if not ret:  # Check if the frame was successfully captured
        print("Failed to capture frame")
        break

    print("ret finish")
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()