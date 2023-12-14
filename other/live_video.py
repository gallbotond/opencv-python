import cv2

# cap = cv2.VideoCapture('http://192.168.0.127:4747/video?640x480')
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FPS, 10)

while(True):
    _, frame = cap.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()