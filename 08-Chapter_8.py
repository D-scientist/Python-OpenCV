# --------- How to Save/Write a video ---------- 

# Import Libraries 

import cv2 as cv
import numpy as mp 

# Loading image from Resource Location

video_capture = cv.VideoCapture("resources\Welcome.mp4")

# Writing Format, Codec, video writer object and file output 

frame_height = int(video_capture.get(3))
frame_width = int(video_capture.get(4))

output = cv.VideoWriter("resources/Out_video.avi",cv.VideoWriter_fourcc("M", "j", 'P', 'G'),10,(frame_width,frame_height),isColor= False)

while(True):
    (ret, frame) = video_capture.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
#  ---- To show in Player
    
    if ret == True:
        
        # write Video
        output.write(grayframe)
        
        # Show Video
        cv.imshow("Video",grayframe)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break



video_capture.release()
output.release()
cv.destroyAllWindows()





