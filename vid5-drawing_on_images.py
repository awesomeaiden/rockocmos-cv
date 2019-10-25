import numpy as np
import cv2

img = cv2.imread('sample_data/lena.jpg', 1)

# Write line on image
# First is image
# Second is start coordinate
# Third is the end coordinate
# Fourth is the color (BGR format)
# Fifth is the thickness
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 4) # Draw blue line on image
img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 255, 0), 4) # Draw green arrow
img = cv2.rectangle(img, (255, 0), (500, 255), (0, 0, 255), -1) # Draw solid red rectangle
img = cv2.circle(img, (300, 300), 30, (255, 0, 255), -1) # Draw circle with center and radius

# Put text on image
# First is image
# Second is text
# Third is starting coordinate
# Fourth is font face
# Fifth is font size
# Sixth is color
# Seventh is thickness
# Eighth is line type
img = cv2.putText(img, "OpenCV", (5, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10, cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0) # Wait for q key
cv2.destroyAllWindows() # close all windows

# You can also create an image using numpy zeros method
# First is height, width, and dimension of array
# Second is data type
img = np.zeros([1000, 1000, 3], np.uint8) # Create black image from numpy array
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Next video - 6 set camera parameters in OpenCV Python