# --------- How To Convert camera video into Different Color Scale


# --------------------STEP-1 import laibraries  

import cv2 as cv
import numpy as np 

# ------------------- STEP-2 Read or Capture Web Cam

cap = cv.VideoCapture(0) # "0" for nWeb Cam No.1 

# --- Error indication
if (cap.isOpened() == False):
    print("Error While finding the Camera")

 

# --------------------- STEP-3 Display the Video Frame By Frame


# read until the end
while(cap.isOpened()):

# return Video into Frame or Capture Frame by Frame 
    ret, frame = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thesh, black_white) = cv.threshold(gray_frame, 127, 255, cv.THRESH_BINARY)
    if ret== True:
        
        # to Show/Display Frame
    
        cv.imshow("Original Cam",frame)
        cv.imshow("Gray",gray_frame)
        cv.imshow("Black & white", black_white)
        
        # Quit Frame window  With q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


# Release or Close Windows 

cap.release()
cv.destroyAllWindows()

