import cv2
import detector as dr
import util

img = cv2.imread('./img/jpg/img1.jpg')
img = cv2.resize(img, None, fx=0.5, fy=0.5)
cv2.imshow('img', img)
cv2.waitKey(0)

# get the height and width of the image
height, width, _ = img.shape
height_crop = 120
width_crop = 10

# crop the image
img = img[height_crop:(height - height_crop), width_crop:(width - width_crop)]
cv2.imshow('cropped', img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
util.display_threshold_window(gray)

# create a trackbar to threshold the image

# save the image to a file
path = 'cropped.jpg'
cv2.imwrite(path, img)

dr.detect_rectangle(path)