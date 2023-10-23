# read a video file and convert it to frames
import cv2
import rescale as rs
import time
import mediapipe as mp

cap = cv2.VideoCapture("./vid/VID_20231010_180634.mp4")


# get the fps of the video
def getFPS(cap):
    fps = cap.get(cv2.CAP_PROP_FPS)
    return fps


frames = []
fps = getFPS(cap)
n = fps / 2

i = 0
j = 0

difference_threshold = 2.5
prev_compare = "same"

hands = mp.solutions.hands.Hands()

# display the frames and take every nth frame
while True:
    _, frame = cap.read()

    if i % n == 0:
        frames.append(frame)
        j += 1
        cv2.imshow("frame", rs.rescaleFrame(frame, 0.2))

        if j > 2:
            img1 = frames[j-1]
            img2 = frames[j-2]
            diff = cv2.absdiff(img1, img2)
            cv2.imshow('diff', diff)
            mean_diff = cv2.mean(diff)[0]

            # determine if there are hands on the frame
            handsDetected = hands.process(frame).multi_hand_landmarks is not None

            if mean_diff < difference_threshold and prev_compare == "different" and not handsDetected:
                # save the current frame to an image file
                cv2.imwrite(f"./curated/frame_{j}_{'%.2f' % mean_diff}.jpg", frame)

            prev_compare = "same" if mean_diff < difference_threshold else "different"

    i += 1
    # wait 1 second for the next frame
    # time.sleep(.1)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# # Load the two images
# img1 = frames[0]
# img2 = frames[1]

# # Compute the absolute difference between the two images
# diff = cv2.absdiff(img1, img2)

# # Display the difference image
# cv2.imshow('Difference', rs.rescaleFrame(diff, .2))

# # Calculate the mean pixel value of the difference image
# mean_diff = cv2.mean(diff)[0]
# print(mean_diff)

# # Determine if the two images are different or not
# if mean_diff < 2:
#     print('The two images are identical')
# else:
#     print('The two images are different')

# cv2.waitKey(0)
cv2.destroyAllWindows()
