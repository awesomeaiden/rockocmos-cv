import cv2
import datetime
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Frame width: " + str(width))
print("Frame height: " + str(height))

while (cap.isOpened()): # Capture frames until program is stopped
    ret, frame = cap.read() # This will return true if the frame is available,
                            # and will save the frame into the frame variable

    if ret == True: # If successfully got the frame
        # Text parameters
        font = cv2.FONT_HERSHEY_SIMPLEX
        location = (100, 50)
        size = 1
        color = (255, 255, 0) # Light Blue
        thickness = 3
        lineType = cv2.LINE_AA
        text = "Width: " + str(width) + " Height: " + str(height)

        # Apply text to frame
        cv2.putText(frame, text, location, font, size, color, thickness, lineType)

        # Show date and time on frame
        datelocation = (100, 100)
        datetext = str(datetime.datetime.now())
        cv2.putText(frame, datetext, datelocation, font, size, color, thickness, lineType)

        # Display the frame
        cv2.imshow("video_capture: " + str(width) + " x " + str(height), frame)

        if cv2.waitKey(1) == ord('q'): # If q key pressed
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()