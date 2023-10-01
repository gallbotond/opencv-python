import cv2 as cv
import rescale as rs
import numpy as np
import matplotlib.pyplot as plt

img = rs.rescaleFrame(cv.imread('./img/1696081363202.jpg'), .1)
# cv.imshow('im', img)

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('rect', rectangle)
cv.imshow('circ', circle)

# bitwise operations
and_op = cv.bitwise_and(rectangle, circle)
or_op = cv.bitwise_or(rectangle, circle)
xor_op = cv.bitwise_xor(rectangle, circle)
not_op = cv.bitwise_not(rectangle)

cv.imshow('and', and_op)
cv.imshow('or', or_op)
cv.imshow('xor', xor_op)
cv.imshow('not', not_op)

cv.waitKey(0)