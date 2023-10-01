import cv2 as cv
import numpy as np
import rescale as rs

img = cv.imread('./img/1696007850854.jpg')
img = rs.rescaleFrame(img, .1)

cv.imshow('img', img)

# translate function
def translate(img, x, y):
  transMatrix = np.float32([[1, 0, x], [0, 1, y]])
  dimensions = (img.shape[1], img.shape[0])
  return cv.warpAffine(img, transMatrix, dimensions)

# rotate function
def rotate(img, angle, rotPoint=None):
  (height, width) = img.shape[:2]
  
  if rotPoint is None:
    rotPoint = (width // 2, height // 2)
    
  rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
  dimensions = (width, height)
  
  return cv.warpAffine(img, rotMat, dimensions)

translated = translate(img, 100, 50)
cv.imshow('translated', translated)

rotated = rotate(translated, 45)
cv.imshow('rotated', rotated)

resized = cv.resize(img, (500, 1000), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

flipped = cv.flip(img, -1) # 1 and 0 for vertical, horizontal, -1 both
cv.imshow('flipped', flipped)


cv.waitKey(0)