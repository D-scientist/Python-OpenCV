# ----------------- How to find Coordinates and Color code from image or Video 

# STEP-1 Import Libraries 

import cv2  as cv 
import numpy as np 

# STEP-2 Define a Function 

def find_coord(event,x,y,flags,perams):
    if event == cv.EVENT_LBUTTONDOWN:
        # LEFT Mouse Click
        print(x,'',y)

        # How to define or print on the same image or window
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x) + ',' +str(y),(x,y), font, 1, (155,0,0),2)

        # Show the Text on image and img itself 
        cv.imshow('Image', img)
    
    # Find Color of Different Objects from an Image 
    if event == cv.EVENT_RBUTTONDOWN:
        # LEFT Mouse Click
        print(x,'',y)

        # How to define or print on the same image or window
        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]

        cv.putText(img, str(b) + ',' + str(g) + ',' + str(r),(x,y), font, 0.5, (155,100,200),2)    
        # Show the Color Code on image and img itself
        cv.imshow("Image", img)
# Final Function 

if __name__ == "__main__":
    
    #reading an Image 
    img = cv.imread('resources\wrap_image.jpeg')
    img = cv.resize(img, (800,800))
    print(img.shape)
    # Display an Image 
    
    cv.imshow('Image', img)
   
    #   Setting Call back Function 
    cv.setMouseCallback('Image', find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()