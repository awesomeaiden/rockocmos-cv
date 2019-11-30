import numpy as np
import cv2

# Looping not working... why

"""
HSV stands for hue, saturation, value.

Problem with RGB is you cannot separate color from luminance.
With HSV, you can.  Hue is shade of the color, saturation is intensity of that
shade, and value is the brightness of the color (0 is black, 1 is full color)
"""

def nothing(x):
    print(x)

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("US", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 0, 255, nothing)

# First convert colored image to hsv image
frame = cv2.imread("sample_data/smarties.png")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

while True:
    # Get trackbar info
    lH = cv2.getTrackbarPos("LH", "Tracking")
    lS = cv2.getTrackbarPos("LS", "Tracking")
    lV = cv2.getTrackbarPos("LV", "Tracking")
    uH = cv2.getTrackbarPos("UH", "Tracking")
    uS = cv2.getTrackbarPos("US", "Tracking")
    uV = cv2.getTrackbarPos("UV", "Tracking")

    # Threshold for blue color
    lowerBound = np.array([lH, lS, lV]) # lower limit
    upperBound = np.array([uH, uS, uV]) # upper limit

    # Generate mask from lower and upper bounds
    mask = cv2.inRange(hsv, lowerBound, upperBound)

    # Generate masked image from mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Show original, mask, and masked original
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()