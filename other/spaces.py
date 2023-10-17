import cv2 as cv
import rescale as rs
import numpy as np
import matplotlib.pyplot as plt

img = rs.rescaleFrame(cv.imread('./img/1696007850854.jpg'), .1)
cv.imshow('im', img)

# plt.imshow(img)
# plt.show()

# bgr to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# bgr to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('lab', lab)

# bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

# hsv to bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr', hsv_bgr)

# lab to bgr
lab_bgr = cv.cvtColor(lab, cv.COLOR_Lab2BGR)
cv.imshow('lab_bgr', lab_bgr)

# grayscale bgr lab
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
bgr_lab = cv.cvtColor(gray_bgr, cv.COLOR_BGR2Lab)
cv.imshow('grayscale bgr lab', bgr_lab)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)