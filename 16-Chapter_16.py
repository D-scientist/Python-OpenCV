# ------ Set Resolution of Camera & Write the video


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
    
def cam_fps():
    cap.set(cv.CAP_PROP_FPS,30)

# We can also set frame rate as 
#    cap.set(5, 30)    

fhd_reolution()

# hd_reolution()
cam_fps()

# or we can also set frame rate 
print('camera frame rate is', cap.get(cv.CAP_PROP_FPS))
   


frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate = int(cap.get(5))
output = cv.VideoWriter("resources/camnew_video.avi",cv.VideoWriter_fourcc('M', 'J', 'P', 'G'),frame_rate,(frame_width,frame_height))

while(True):
     (ret, frame) = cap.read()

# ---------------- WE CAN ALSO CHANGE THE FRAME SIZE BY THIS WAY    
    
    #  frame = cv.resize(frame, None, None, fx=1.2, fy=1.0)
     
     grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
     hsvframe = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
  
# #  ---- To show in Player
    
     if ret == True:
        
         # write Video
         output.write(frame)
         # Show Video
         cv.imshow("Video",grayframe)
         cv.imshow('Orginal',frame)
         cv.imshow('HSV', hsvframe)
         
         if cv.waitKey(1) & 0xFF == ord('q'):
             break
     else:
         break

video_capture.release()
output.release()
cv.destroyAllWindows()
