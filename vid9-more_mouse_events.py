import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

# Standard callback function to handle click events
def clickEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        cv2.circle(img, (x, y), 3, (255, 255, 0), -1, cv2.LINE_AA) # Show filled circle
        points.append((x, y)) # add point to points array
        if (len(points) >= 2): # If clicked 2 times or more, draw a line between the last 2 points
            cv2.line(img, points[-2], points[-1], (0, 255, 255), 2, cv2.LINE_AA)

    elif event == cv2.EVENT_RBUTTONDOWN:
        while(len(points)):
            points.pop()

    cv2.imshow("circles", img)

img = np.zeros((1000, 1000, 3), np.uint8)
cv2.imshow("circles", img)

# Declare array to store points clicked
points = []

cv2.setMouseCallback("circles", clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Next vid: vid10 cv.split, cv.merge...