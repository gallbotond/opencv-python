import cv2 as cv
import rescale as rs
import numpy as np

img = rs.rescaleFrame(cv.imread('./img/1696007850854.jpg'), .1)

cv.imshow('im', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur) 

canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contours found')

# another method
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (200, 200, 0), 1)
cv.imshow('contours', blank)

cv.waitKey(0)