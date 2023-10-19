import picamera
import cv2
import numpy as np

# Create a PiCamera object
camera = picamera.PiCamera()
camera.resolution = (640, 480)  # Set the resolution as desired

# Get the camera's hardware revision
camera_revision = camera.revision
# Get the camera's unique serial number
camera_serial = camera.serial

print(f"Camera Revision: {camera_revision}")
print(f"Camera Serial: {camera_serial}")

# Create an OpenCV window
cv2.namedWindow("Raspberry Pi Camera", cv2.WINDOW_NORMAL)

try:
    while True:
        # Capture a frame from the Raspberry Pi camera
        stream = io.BytesIO()
        camera.capture(stream, format='jpeg')
        data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        frame = cv2.imdecode(data, 1)

        # Display the frame in an OpenCV window
        cv2.imshow("Raspberry Pi Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Close the OpenCV window and release the camera
    cv2.destroyAllWindows()
    camera.close()