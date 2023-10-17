import cv2 as cv
import rescale as rs
import numpy as np
import matplotlib.pyplot as plt

img = rs.rescaleFrame(cv.imread('./img/1696081363202.jpg'), .1)
cv.imshow('im', img)

blank = np.zeros(img.shape[:2], dtype="uint8")

b, g, r = cv.split(img) 

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('r', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow("merged", merged)

cv.waitKey(0)