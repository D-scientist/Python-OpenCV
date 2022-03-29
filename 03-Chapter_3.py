
# ------ Conversion In Grey-Scale -------



# library impo

import numpy as np
import cv2 as cv

img_object = cv.imread("resources/bike.jpg")

# Resize the image window (height & width)

img_object = cv.resize(img_object, (800,600))

# --- Conversion In Grey-Scale
gray_img = cv.cvtColor(img_object,cv.COLOR_BGR2GRAY)

# Show image 

cv.imshow("Object_image", img_object)
cv.imshow("Gray image",gray_img)


# delay Code ( in miliseconds)
cv.waitKey(0)

# Destroy All Windows

cv.destroyAllWindows()


