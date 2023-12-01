import cv2

def display_threshold_window(image):
    # Create a window to display the image
    cv2.namedWindow('Threshold Image')

    # Set an initial threshold value
    initial_threshold = 128

    def on_threshold_change(value):
        # Apply thresholding to the image
        _, thresholded_image = cv2.threshold(image, value, 255, cv2.THRESH_BINARY)

        # Display the thresholded image
        cv2.imshow('Threshold Image', thresholded_image)

    # Create a trackbar for the threshold value
    cv2.createTrackbar('Threshold', 'Threshold Image', initial_threshold, 255, on_threshold_change)

    # Initialize the thresholded image
    thresholded_image = cv2.threshold(image, initial_threshold, 255, cv2.THRESH_BINARY)[1]

    # Display the thresholded image
    cv2.imshow('Threshold Image', thresholded_image)

    # Wait for a key press
    cv2.waitKey(0)

    # Destroy the window
    cv2.destroyAllWindows()