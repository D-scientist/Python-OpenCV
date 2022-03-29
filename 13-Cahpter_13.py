# --------- Basic Function Or Manipulation in OpenCv


import cv2 as cv 
import numpy as np 

img= cv.imread('resources/lion-4k.jpg')

# Resize 
resized_img = cv.resize(img, (45,250))

# Gray 

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Black & White 

(thresh,black_white) = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

# Blurred Image
blurr_img = cv.GaussianBlur(img, (53,53), 0)


# Edge Detection 

edge_img = cv.Canny(img, 150, 100)

# Thinkness Of Lines 
mat_kernel = np.ones((1,1), np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernel), iterations=1)

# Make Thinner Outline (Erosion)

ero_img = cv.erode(dilated_img, mat_kernel, iterations=1)  

# Cropping an image 
print("The size of our Image is:", img.shape)
cropped_img = img[50:320,200:500]


cv.imshow('Original',img)
cv.imshow('Resized Image',resized_img)
cv.imshow('Gray Image', gray_img)
cv.imshow('Black & White', black_white)
cv.imshow('Blurred Image',blurr_img)
cv.imshow('Edge Detection Image',edge_img)
cv.imshow('Dilated Image', dilated_img)
cv.imshow('Erosion Image', ero_img)
cv.imshow("Cropped Image", cropped_img)


cv.waitKey(0) 
cv.destroyAllWindows()   