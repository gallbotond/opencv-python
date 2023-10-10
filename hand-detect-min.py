import cv2
import mediapipe as mp
import rescale as rs

# cap = cv2.VideoCapture("http://192.168.0.127:4747/video?640x480")
cap = cv2.VideoCapture("./vid/VID_20231010_180634.mp4")

# function to get the fps of the video
def getFPS(cap):
  fps = cap.get(cv2.CAP_PROP_FPS)
  return fps

# function to convert the video to 10 fps based on the fps of the video
def convertTo10FPS(video):
    fps = getFPS(video)
    new_fps = 10
    frame_interval = int(fps / new_fps)
    
    frames = []
    count = 0
    while True:
      success, frame = video.read()
      if not success:
        break
      if count % frame_interval == 0:
        frames.append(frame)
        cv2.imshow('10fps', rs.rescaleFrame(frame, .2))
        cv2.waitKey(1)
      count += 1
      print("processed frame", count)
    
    return frames

# function to remove frames with hands
def removeFramesWithHands(cap10fps):
  newCap10fps = []

  for frame in cap10fps:
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks == None:
      newCap10fps.append(frame)
      print ("No hands")
    else:
       print ("Hands")
    
    # cv2.imshow("Image", rs.rescaleFrame(frame, .2))
    
  return newCap10fps

print("FPS: ", getFPS(cap))
# cv2.waitKey(1)

cap10fps = convertTo10FPS(cap)

# detect hands in images or video streams 
mpHands = mp.solutions.hands
hands = mpHands.Hands()

cap10fpsNoHands = removeFramesWithHands(cap10fps)

fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # or other codec
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# save cap10fpsNoHands as a video file
for frame in cap10fpsNoHands: 
  cv2.imshow("handless", rs.rescaleFrame(frame, .2))
   
  if cv2.waitKey(1) & 0xff == ord('q'):
    break

  out.write(frame)


out.release()
cv2.destroyAllWindows()