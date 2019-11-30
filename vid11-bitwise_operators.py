import cv2
import numpy as np

img2 = cv2.imread("sample_data/building.jpg") # Image from picture file
img1 = np.zeros(img2.shape, np.uint8) # Create black image from empty numpy array (match size of img2)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1) # Create rectangle on image 1

# This will create an image that combines the image with AND logic
# Basically all black except for the rectangle (when both images have nonzero content)
bitAnd = cv2.bitwise_and(img1, img2)

# Combine both images with OR logic (one or the other)
bitOr = cv2.bitwise_or(img1, img2)

# Combine both images with XOR logic (exclusively one or the other)
bitXOr = cv2.bitwise_xor(img1, img2)

# Combine both images with NOT logic (opposite of inputted image)
bitNot = cv2.bitwise_not(img2)

# Show pictures
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAnd", bitAnd)
cv2.imshow("bitOr", bitOr)
cv2.imshow("bitXOr", bitXOr)
cv2.imshow("bitNot", bitNot)

# Wait for q key to be pressed
cv2.waitKey(0)
cv2.destroyAllWindows()