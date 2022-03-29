# --------- How To Capture a Web Cam inside Python


# --------------------STEP-1 import laibraries  

import cv2 as cv
import numpy as np 

# ------------------- STEP-2 Read or Capture Web Cam
 
cap = cv.VideoCapture(0) # "0" for nWeb Cam No.1 

# --- Error indication
if (cap.isOpened() == False):
    print("There is an error")

 

# --------------------- STEP-3 Display the Video Frame By Frame


# read until the end
while (cap.isOpened()):

# return Video into Frame or Capture Frame by Frame 
    ret, frame = cap.read()
    if ret == True:
        
        # to Show/Display Frame
        cv.imshow("Video",frame)
        
        # Quit Fframe window  With q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


# Release or Close Windows 

cap.release()
cv.destroyAllWindows()

