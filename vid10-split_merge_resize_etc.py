import numpy as np
import cv2

img = cv2.imread("sample_data/messi5.jpg")
img2 = cv2.imread("sample_data/opencv-logo.png")

print("Shape:", img.shape) # print a tuple of number of rows, columns, and channels in image
print("Size:", img.size) # returns total number of pixels in the image
print("Data type:", img.dtype) # returns the datatype of the image

# split into three channels
b,g,r = cv2.split(img)

# merge channels into an image
img = cv2.merge((b, g, r))

# get one section of the image
ball = img[280:340, 330:390]

# Copy that section of the image to another spot on the image
img[273:333, 100:160] = ball

# Resize images to same size for addition
img = cv2.resize(img, (500, 500))
img2 = cv2.resize(img2, (500, 500))

# Add two images to each other
combined = cv2.add(img, img2)

# Add (weighted) two images to each other (first image, first image weight, second image, second image weight, and scalar offset value)
combined = cv2.addWeighted(img, 0.75, img2, .25, 0)

cv2.imshow("image", img)
cv2.imshow("image2", img2)
cv2.imshow("resized", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

# next vid: vid11 bitwise operations