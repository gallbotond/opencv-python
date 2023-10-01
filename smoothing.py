import cv2 as cv
import rescale as rs
import numpy as np
import matplotlib.pyplot as plt

img = rs.rescaleFrame(cv.imread('./img/1696081363202.jpg'), .1)
cv.imshow('im', img)

# averaging
avg = cv.blur(img, (7, 7))
cv.imshow('average blur', avg)

# gaussian 
gaus = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('gaus', gaus)

# median
median = cv.medianBlur(img, 7)
cv.imshow('median', median)

# bilateral 
bi = cv.bilateralFilter(img, 10, 50, 50)
cv.imshow('bilateral', bi)

cv.waitKey(0)