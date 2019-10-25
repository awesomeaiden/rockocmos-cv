import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

# Standard callback function to handle click events
def clickEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        coords = str(x) + ", " + str(y)
        cv2.putText(img, coords, (x, y), font, 1, (255, 255, 0), 2)
        cv2.imshow("click_location", img)

    elif event == cv2.EVENT_RBUTTONDOWN:
        blueChan = img[y, x, 0]
        greenChan = img[y, x, 1]
        redChan = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        channels = str(blueChan) + ", " + str(greenChan) + ", " + str(redChan)
        cv2.putText(img, channels, (x, y), font, 1, (0, 255, 255), 2)
        cv2.imshow("click_location", img)

img = np.random.rand(1000, 1000, 3)
cv2.imshow("click_location", img)

cv2.setMouseCallback("click_location", clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()