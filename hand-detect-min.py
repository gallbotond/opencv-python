import cv2
import mediapipe as mp
import rescale as rs

# cap = cv2.VideoCapture("http://192.168.0.127:4747/video?640x480")
cap = cv2.VideoCapture("./vid/VID_20230929_200847.mp4")

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
  success, img = cap.read()
  
  imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  results = hands.process(imgRGB)

  print("hands detected" if results.multi_hand_landmarks != None else "no hands")
  
  cv2.imshow("Image", rs.rescaleFrame(img, .2))
  cv2.waitKey(1)