import cv2
import numpy as np

# load input image
img = cv2.imread('./img/jpeg/im1.jpeg')

# convert to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# downscale image
img = cv2.resize(img, (img.shape[1]//8, img.shape[0]//8))

# set up the detector with default parameters
detector = cv2.SimpleBlobDetector_create()

# detect blobs
keypoints = detector.detect(img)

# draw detected blobs as red circles
blank_img = np.zeros((1, 1))
blobs = cv2.drawKeypoints(img, keypoints, blank_img, (0, 0, 255),
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# show keypoints
cv2.imshow("Blobs", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()