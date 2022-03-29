# -------------- Reading a Video -----------



# Import Libraries 

import cv2 as cv
import numpy as mp 

# Loading image from Resource Location

video_capture = cv.VideoCapture("resources\Welcome.mp4")

# Indicator 
if (video_capture.isOpened()== False):
    print("Error in reading video")

# reading and Playing
while(video_capture.isOpened()):
    ret , frame = video_capture.read()
    if ret == True:
        cv.imshow("Video",frame)
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