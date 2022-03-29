 
#  How to change the perspective of an image

import cv2 as cv 
import numpy as np 

img = cv.imread('resources\wrap_image.jpeg')
img = img.resize(800,800)


#  Defining Points 

point1 = np.float32([[73,99],[670,113],[17,596],[789,574]])

height,width = 800,800

point2 = np.float32([[0,0], [800,0], [0,height], [width,height]])

# point2 = np.float32([[0,0],[0,1600],[900,0],[width,height]])

matrix = cv.getPerspectiveTransform(point1,point2)

out_img = cv.warpPerspective(img, matrix, (width,height))


cv.imshow('winname', img)
cv.imshow('Transformed',out_img)
cv.waitKey(0)
cv.destroyAllWindows()