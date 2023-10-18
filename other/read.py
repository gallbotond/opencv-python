import cv2 as cv

# read image
img = cv.imread('./img/1696007850854.jpg')

cv.imshow('image', img)

cv.waitKey(0)


# read video
capture = cv.VideoCapture(0)

while True:
  isTrue, frame = capture.read()
  cv.imshow('video', frame)
  
  if cv.waitKey(20) & 0xff == ord('d'):
    break
  
capture.release()
cv.destroyAllWindows()