# -------------- Img Conversion into Black & White -----------



# Import Libraries 

import cv2 as cv
import numpy as mp 

# Loading image from Resource Location

img = cv.imread("resources/bike.jpg")

img = cv.resize(img, (900,600))

# first we will convert into gray Color

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Converting into binary or Black & White 

(thesh, black_white) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# Show Image 

cv.imshow("Color Tasveer Original", img)
cv.imshow("gray",gray)
cv.imshow("Color Tasveer Original", black_white)

# Delay 

cv.waitKey(0)
destroyAllWindows()