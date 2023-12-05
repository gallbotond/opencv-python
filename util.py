import cv2
import numpy as np

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

    # Get the final threshold value
    final_threshold = cv2.getTrackbarPos('Threshold', 'Threshold Image')
    return final_threshold

def custom_div(im1, im2):
    result = np.zeros((im1.shape[0], im1.shape[1]), dtype='uint8')
    # iterate over the whole image and subtract im2 from im1
    for i in range(im1.shape[0]):
        for j in range(im1.shape[1]):
            val1 = im1[i][j].astype('int8')
            val2 = im2[i][j].astype('int8')
            res = val1 - val2
            # make sure the value is not negative
            if res < 0:
                result[i][j] = 0
            else:
                result[i][j] = res

    return result