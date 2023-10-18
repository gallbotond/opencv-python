import cv2 as cv
import rescale as rs
import numpy as np

videoCapture = cv.VideoCapture('http://192.168.0.105:4747/video?1920x1080')
prevCircle = None
dist = lambda x1,y1,x2,y2: (x1 - x2)**2 + (y1 - y2)**2

while True:
  ret, frame = videoCapture.read()
  if not ret: break
  
  # frame = cv.imread('img/1696081363202.jpg')
  
  grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  blurFrame = cv.GaussianBlur(grayFrame, (17,17), 0)
  
  # 
  circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 1, param1=50, minRadius=1, maxRadius=100)

  if circles is not None:
    circles = np.uint16(np.around(circles))
    chosen = None
    for i in circles[0, :]:
      if chosen is None: chosen = i
      if prevCircle is not None:
        if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
          chosen = i
      cv.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
      cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
      prevCircle = chosen
      
  cv.imshow("circles", rs.rescaleFrame(frame, .8))
  
  if cv.waitKey(1) & 0xff == ord('q'): break
  
videoCapture.release()
cv.destroyAllWindows()