import cv2 as cv


# rescale function
def rescaleFrame(frame, scale=.5):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  
  dimensions = (width, height)
  
  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# change resolution of live video
def changeRes(width, height):
  capture.set(3, width)
  capture.set(4, height)
  

# # read and rescale image
# img = cv.imread('./img/1696007850854.jpg')

# img = rescaleFrame(img, .2)

# cv.imshow('image', img)
# cv.waitKey(0)

# # read and rescale video, filename for media and index number for live camera
# capture = cv.VideoCapture('./vid/VID_20230929_200847.mp4')

# while True:
#   isTrue, frame = capture.read()
  
#   resized_frame = rescaleFrame(frame, .3)
  
#   cv.imshow('video', frame)
#   cv.imshow('video_resized', resized_frame)
  
#   if cv.waitKey(20) & 0xff == ord('d'):
#     break
  
# capture.release()
# cv.destroyAllWindows()