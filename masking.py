import cv2 as cv
import rescale as rs
import numpy as np
import matplotlib.pyplot as plt

img = rs.rescaleFrame(cv.imread('./img/1696081363202.jpg'), .1)
# cv.imshow('im', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 50, 255, -1)
# cv.imshow('mask', mask)

x = img.shape[1] // 2
y = img.shape[0] // 2

circle = cv.circle(blank.copy(), (x, y), 50, 255, -1)
square = cv.rectangle(blank.copy(), (x, y - y // 2), (x + x // 2, y + y // 2), 255, -1)

shape = cv.bitwise_and(circle, square)

cv.imshow("shape", shape)

masked = cv.bitwise_and(img, img, mask = shape)
cv.imshow('masked image', masked)

cv.waitKey(0)