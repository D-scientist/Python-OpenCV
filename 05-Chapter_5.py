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

black_white = cv.resize(black_white, (700,400))


# Saving an Image or Writing an image 

cv.imwrite("resources\BikeImage_gray.png",gray)
cv.imwrite("resources\BikeImage_bw.png",black_white)


# Show Image 

# cv.imshow("Color Tasveer Original", img)
# cv.imshow("gray",gray)


# Delay 

cv.waitKey(0)
cv.destroyAllWindows()