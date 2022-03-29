# -------------- Converting Video to gray or Black & White -----------



# Import Libraries 

import cv2 as cv
import numpy as mp 

# Loading image from Resource Location

video_capture = cv.VideoCapture("resources\Welcome.mp4")


while(True):
    (ret, frame) = video_capture.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
#  ---- To show in Player
    
    if ret == True:
        cv.imshow("Video",grayframe)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break



video_capture.release()
cv.destroyAllWindows()





# Delay 

cv.waitKey(0)
cv.destroyAllWindows()



# -------------- # Code for converting into Black & White -----------



# Import Libraries 

import cv2 as cv
import numpy as mp 

# Loading image from Resource Location

video_capture = cv.VideoCapture("resources\Welcome.mp4")


while(True):
    (ret, frame) = video_capture.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Code for converting into Black & White 
    (thesh, black_white) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)
    
    if ret == True:
        cv.imshow("Video",black_white)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break



video_capture.release()
cv.destroyAllWindows()


# Show Image 

# cv.imshow("Color Tasveer Original", img)
# cv.imshow("gray",gray)


# Delay 

cv.waitKey(0)
cv.destroyAllWindows()
