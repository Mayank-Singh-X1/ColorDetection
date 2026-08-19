import cv2
from PIL import Image
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to open camera")
    raise SystemExit(1)

#Bounds for yellow color
lower_bound = np.array([20, 110, 60])
upper_bound = np.array([35, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read from camera")
        break

    # convert to hsv
    hsvimage= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsvimage, lower_bound, upper_bound )

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox() #bounding box

    if bbox is not None:
        x1,y1,x2,y2 = bbox
        frame  = cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 255, 255), 4)
    

    cv2.imshow('frame', frame)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()