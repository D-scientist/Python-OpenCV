# ------ How to Draw Lines, And Shapes on Images 
import cv2 as cv 
import numpy as np 


# Draw a Canvas
img= np.zeros((500,700))
img1=np.ones((500,600))
print(img.shape)

# print(img)

# Adding Colors to Camvas
colored_img = np.zeros((600,600,3), np.uint8)
# Selecting Complete Image Via Indexing 
colored_img[:] = 20,50,100 
# Selecting Small Portion of the Image 

colored_img[100:200,200:300] = 90,80,150 

# Adding Line 
cv.line(colored_img,(0,0),(200,300),(255,120,3),3)
cv.line(colored_img,(0,0),(colored_img.shape[0],colored_img.shape[1]),(255,100,150),3)

# Adding Ractangles
cv.rectangle(colored_img, (100,250), (300,400), (255,200,150),3)
cv.rectangle(colored_img, (100,250), (300,400), (255,200,150), cv.FILLED)

# Adding Circle
cv.circle(colored_img, (300,400), 50, (90,100,100),10)
cv.circle(colored_img, (300,400), 50, (90,100,100),cv.FILLED)

# Adding Text
# cv.putText(img, text, org, fontFace, fontScale, color)
# cv.putText(colored_img, '''' Adding Shape and Lines \n in Image Using Open Cv ''', (80,550), cv.FONT_HERSHEY_PLAIN, 1, (100,100,100),2)

text = " Adding Shape and Lines \n in Image Using Open Cv \n M.Tanzeel"
y0, dy = 500, 30
for i, line in enumerate(text.split('\n')):
    y = y0 + i*dy
    cv.putText(colored_img, line, (80, y ), cv.FONT_HERSHEY_SIMPLEX, 1, (100,100,100),2)

# cv.imshow("Images", img)
# cv.imshow("White Image",img1)

cv.imshow("colored_img", colored_img)
cv.waitKey(0) 
cv.destroyAllWindows() 