 # --------- How to Save/Write a video from Web Cam ---------- 

 # Import Libraries 

import cv2 as cv
import numpy as np 

 # Loading image from Resource Location

video_capture = cv.VideoCapture(0)

 # Writing Format, Codec, video writer object and file output 

# frame_height = int(video_capture.get(4))
# frame_width = int(video_capture.get(3))

fourcc=cv.VideoWriter_fourcc('M','J','P','G')
output= cv.VideoWriter("resources/webcam_video_resize.avi",fourcc,20.0,(640,480))

# output = cv.VideoWriter("resources/cam_video.avi",cv.VideoWriter_fourcc('M', 'J', 'P', 'G'),60,(frame_width,frame_height))

while(True):
     (ret, frame) = video_capture.read()

# ---------------- WE CAN ALSO CHANGE THE FRAME SIZE BY THIS WAY    
    
    #  frame = cv.resize(frame, None, None, fx=1.2, fy=1.0)
     
     grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  
# #  ---- To show in Player
    
     if ret == True:
        
         # write Video
         output.write(frame)
         # Show Video
         cv.imshow("Video",grayframe)
         cv.imshow('Orginal',frame)
         if cv.waitKey(1) & 0xFF == ord('q'):
             break
     else:
         break

video_capture.release()
output.release()
cv.destroyAllWindows()





