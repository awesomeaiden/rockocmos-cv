import cv2

# Reading an image
# There is no exception thrown here if the filename is invalid.
# In case the filename is wrong, you can check the returned value from
# imread() and throw an error
image = cv2.imread("sample_data/lena.jpg", cv2.IMREAD_UNCHANGED)

# If image is None (not successfully opened, probably file path issue)
if (not image.any()):
    print("filename is invalid")
else:
    print("filename is valid and image opened successfully:")
    print(image) # Prints image out as array
    cv2.imshow("window_name", image) # Shows the image for a split second
    cv2.waitKey(3000) # Show the image for 3 seconds before closing window
    cv2.destroyAllWindows() # Get rid of all windows created

# Write image in form of file
cv2.imwrite("image_name.png", image)

# Show image again to demonstrate key closing
cv2.imshow("new_window_name", image)
waitKey = cv2.waitKey(0) # Show the image indefinitely

# If escape key pressed
if waitKey == 27:
    cv2.destroyAllWindows()
elif waitKey == ord("s"): # If s key pressed
    cv2.imwrite("s_key_image_name.png", image)
    cv2.destroyAllWindows()

# Next video: vid 4 on videos from camera