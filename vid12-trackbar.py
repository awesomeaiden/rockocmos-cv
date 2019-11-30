import numpy as np
import cv2
import time

# Create a black image
img = np.zeros((500, 500, 3), np.uint8)
cv2.namedWindow("image")

def blue(x):
    img[:][:][0] = x

def green(x):
    img[:][:][1] = x

def red(x):
    img[:][:][2] = x

def output(x):
    print(x)

# Create trackbar named "B" in the named window "image"
cv2.createTrackbar("B", "image", 0, 255, output)
cv2.createTrackbar("G", "image", 0, 255, output)
cv2.createTrackbar("R", "image", 0, 255, output)

while 1:
    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv2.getTrackbarPos("B", "image")
    g = cv2.getTrackbarPos("G", "image")
    r = cv2.getTrackbarPos("R", "image")

    img[:] = [b, g, r]

cv2.destroyAllWindows()