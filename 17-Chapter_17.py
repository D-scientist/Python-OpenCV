# ------- Joing Two Images ---



import cv2 as cv 
import numpy as np 

img = cv.imread("resources\Bikeimage_gray.png")

img1 = cv.imread('resources\lion-4k.jpg')

# ver_stack = np.vstack((img,img1))
# hor_stack = np.hstack((img,img1))


# # cv.imshow('Vertical Stack',ver_stack)
# cv.imshow('Vertical Stack',hor_stack)



# -----------------define a function for vertically
# concatenating/Join images of different widths

def vconcat_resize(img_list, interpolation
				= cv.INTER_CUBIC):
	# take minimum width
	w_min = min(img.shape[1]
				for img in img_list)
	
	# resizing images
	im_list_resize = [cv.resize(img,
					(w_min, int(img.shape[0] * w_min / img.shape[1])),
								interpolation = interpolation)
					for img in img_list]
	# return final image
	return cv.vconcat(im_list_resize)

# function calling
img_v_resize = vconcat_resize([img, img1,img])

# show the output image
cv.imwrite('resources/vconcat_resize.jpg', img_v_resize)
cv.imshow('vconcat_resize.jpg', img_v_resize)


# -------------------------------define a function for horizontally concatenating/Joning images of different
# heights
def hconcat_resize(img_list,
				interpolation
				= cv.INTER_CUBIC):
	# take minimum hights
	h_min = min(img.shape[0]
				for img in img_list)
	
	# image resizing
	im_list_resize = [cv.resize(img,
					(int(img.shape[1] * h_min / img.shape[0]),
						h_min), interpolation
								= interpolation)
					for img in img_list]
	
	# return final image
	return cv.hconcat(im_list_resize)

# function calling
img_h_resize = hconcat_resize([img1, img, img])

# show the Output image
cv.imshow('hconcat_resize.jpg', img_h_resize)
cv.imwrite('resources\hor_join.jpg', img_h_resize)

cv.waitKey(0)
cv.destroyAllWindows()