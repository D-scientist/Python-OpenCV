# ----------- Setting of Camera Frame or Video

import cv2 as cv
import numpy as np 
cap = cv.VideoCapture(0)
cap.set(3, 640) # 3 is key for Width
cap.set(4, 480) # 4 is key for height Value
cap.set(10, 100) # 10 is key foe Brightness
while (True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('Original', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()    

