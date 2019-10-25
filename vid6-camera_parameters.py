import cv2

cap = cv2.VideoCapture(0)

# Print properties before changing
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Can also set these properties
# Won't go exactly to these dimensions sometimes because the camera will use the closest compatible resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Print properties after changing
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Save properties
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Similar frame display code as before
while (cap.isOpened()): # Capture frames until program is stopped
    ret, frame = cap.read() # This will return true if the frame is available,
                            # and will save the frame into the frame variable

    if ret == True: # If successfully got the frame
        cv2.imshow("video_capture: " + str(width) + " x " + str(height), frame)

        if cv2.waitKey(1) == ord('q'): # If q key pressed
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()