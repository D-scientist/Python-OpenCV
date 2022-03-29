# library impo

import numpy as np
import cv2 as cv

# loading image from resource

img_object = cv.imread("resources/bike.jpg")

# Resize the image window (height & width)

img_object2 = cv.resize(img_object, (500,600))

# Show image 

cv.imshow("Object_image", img_object)

cv.imshow("Object_image", img_object2)

# delay in miliseconds
cv.waitKey(0)

# Destroy All Windows
# cv.destroyAllWindows()


