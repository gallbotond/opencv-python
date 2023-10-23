# read a video file and convert it to frames
import cv2
import rescale as rs
import time
import mediapipe as mp
import datetime
import os
import matplotlib.pyplot as plt

file_name = "./vid/short-sample2.mp4"

cap = cv2.VideoCapture(file_name)

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

# Create an empty plot
fig, ax = plt.subplots()

plot_diff = []
x = []

line, = ax.plot(x, plot_diff)

hands = mp.solutions.hands.Hands()

# create a new folder with the day, hour and minute as the folder name
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")

if not os.path.exists(current_time):
    os.makedirs(f'./data/{current_time}')

# display the frames and take every nth frame
while True:
    _, frame = cap.read()

    if i % n == 0:
        frames.append(frame)
        j += 1
        cv2.imshow("frame", rs.rescaleFrame(frame))

        if j > 3:
            img1 = frames[j-1]
            img2 = frames[j-2]
            diff = cv2.absdiff(img1, img2)
            mean_diff = cv2.mean(diff)[0]

            # determine if there are hands on the frame
            handsDetected = hands.process(frame).multi_hand_landmarks is not None

            if (
                    mean_diff1 < difference_threshold 
                    and mean_diff2 < difference_threshold
                    and prev_compare == "different" 
                    and not handsDetected
                ):
                # save the current frame to an image file
                cv2.imwrite(f"./data/{current_time}/frame_{j}_{'%.2f' % mean_diff1}.jpg", frame)
                print("saved")

            prev_compare = "same" if mean_diff1 < difference_threshold and mean_diff2 < difference_threshold else "different"

    i += 1
    # wait 1 second for the next frame
    # time.sleep(.1)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# plot the mean diff
plt.plot(plot_diff)
plt.show()

cv2.destroyAllWindows()

# save the fps, threshold, and file name to a csv file
with open(f"./data/{current_time}/data.csv", "w") as f:
    f.write("fps, threshold, file_name\n")
    f.write(f"{fps}, {difference_threshold}, {current_time}\n")