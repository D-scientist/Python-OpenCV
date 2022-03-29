# library import
import cv2 as cv 

img_object = cv.imread("resources/bike.jpg")

# Show image 

cv.imshow("Object_image", img_object)
cv.waitKey(0)
# destroy All Windows()
cv.destroyAllWindows()

