# ------ Resolution of Camera


import cv2 as cv 
import numpy as np 

# STEP-2 ------------------ capture Camera

cap = cv.VideoCapture(0)

# STEP-3 ---------------- Camera Frame setting
  
# Set Resolution HD (1280 x 720) Using Function 

def hd_reolution ():
    cap.set(3, 1280)
    cap.set(4, 720)

def fhd_reolution ():
    cap.set(3, 1920)
    cap.set(4, 1080)
# ------ Assignment ---------   
def cam_fps():
    cap.set(cv.CAP_PROP_FPS,30)

# We can also set frame rate as 
#    cap.set(5, 30) 
# ------ Assignment ---------   

fhd_reolution()

# hd_reolution()
cam_fps()

# or we can also set frame rate 
print('camera frame rate is', cap.get(cv.CAP_PROP_FPS))
   

# STEP-3  Display Camera 

while(True):
    ret , frame = cap.read()
    if ret == True:
        cv.imshow('Camera',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break 
    else:
        break
print('camera frame rate is', cap.get(cv.CAP_PROP_FPS))
cap.release()
cv.destroyAllWindows()