import cv2 as cv
import rescale as rs
import time

img = cv.imread('./img/1696007850854.jpg')

# resc
img = rs.rescaleFrame(img, .1)
cv.imshow('color', img)

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# edge cascade
for i in range(0, 3):
  canny = cv.Canny(blur, i * 50, i * 100)
  cv.imshow(f'canny edges {i}', canny)
  
# dilate
dilated = cv.dilate(canny, (10, 10), iterations=5)
cv.imshow('dilated', dilated)

# erode
eroded = cv.erode(canny, (5, 5), iterations=1)
cv.imshow('eroded', eroded)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# crop
cropped = img[0:200, 0:200]
cv.imshow('cropped', cropped)


cv.waitKey(0)