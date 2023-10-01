import cv2 as cv
import numpy as np

# create new img, with 500px width and height and 3 color channels
blank = np.zeros((500, 500, 3), dtype='uint8')

# cv.imshow('Blank', blank)

# draw shapes
cv.rectangle(blank, (50, 50), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=2)

cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness=1)

cv.line(blank, (0, 0), (40, 200), (255, 255, 255), thickness=3)

# put text
cv.putText(blank, 'Hello', (249, 276), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)

cv.imshow('shapes', blank)

# img = cv.imread('./img/1696007850854.jpg')
# cv.imshow('cat', img)

# change the color
blank[:] = 100, 55, 200

# draw a rectangle to coordinates
blank[200:300, 300:400] = 200, 100, 55
cv.imshow('Green', blank)

cv.waitKey(0)