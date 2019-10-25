import cv2

# cap = cv2.VideoCapture("video.mp4") # For video
cap = cv2.VideoCapture(0) # Default camera index

# Get desired fourcc code
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# out is output class
# First is name of output file
# Second is video codec (fourcc)
# Third is frames per second
# Fourth is size of video captured
out = cv2.VideoWriter('test_samples/output.avi', fourcc, 20.0, (640,480))

# while (cap.isOpened()) # Can use this for running while video is open
# cap.open() can open the capture video
# cap.get() can get a given property from the video capture

while (True): # Capture frames until program is stopped
    ret, frame = cap.read() # This will return true if the frame is available,
                            # and will save the frame into the frame variable

    if ret == True: # If successfully got the frame
        # Make new frame by converting frame from RGB to Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Get the frame width and print it out
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        # Output a color frame to the video writer
        out.write(frame)

        # Show grayscale frame in window
        cv2.imshow("name_of_window_for_frame", gray)

        if cv2.waitKey(1) == ord('q'): # If q key pressed
            break
    else:
        break

# Now release resources
cap.release()
out.release()
cv2.destroyAllWindows()