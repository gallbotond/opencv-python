# read a video file and convert it to frames
import cv2
import rescale as rs
import time
import mediapipe as mp
import datetime
import os
import matplotlib.pyplot as plt

file_name = "./vid/short-sample4.mp4"

cap = cv2.VideoCapture(file_name)

# get the fps of the video
def getFPS(cap):
    fps = cap.get(cv2.CAP_PROP_FPS)
    return fps

# get the frame count of the video
def getFrameCount(cap):
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    return frame_count

fpsToCapture = 2

frameCount = getFrameCount(cap)
frames = []
fps = getFPS(cap)
n = fps / fpsToCapture

i = 0
j = 0

difference_threshold = 5.0
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

# save the fps, threshold, and file name to a csv file
with open(f"./data/{current_time}/data.csv", "w") as f:
    f.write("sample_fps, fps_to_capture,  threshold, file_name\n")
    f.write(f"{fps}, {fpsToCapture}, {difference_threshold}, {file_name}\n")

# display the frames and take every nth frame
while i < frameCount:
    _, frame = cap.read()

    if i % n == 0:
        frames.append(frame)
        j += 1
        cv2.imshow("frame", rs.rescaleFrame(frame))

        if j > 3:
            img1 = frames[j-1]
            img2 = frames[j-2]
            img3 = frames[j-3]

            diff1 = cv2.absdiff(img1, img2)
            diff2 = cv2.absdiff(img2, img3)

            # diff = cv2.bitwise_and(diff1, diff2)

            mean_diff1 = cv2.mean(diff1)[0]
            mean_diff2 = cv2.mean(diff2)[0]
            
            print(mean_diff1, mean_diff2, prev_compare)

            # plot the plot_diff and show it
            x.append(j)
            plot_diff.append(mean_diff1)
            line.set_data(x, plot_diff)

            ax.relim()
            ax.autoscale_view()

            plt.draw()
            plt.pause(0.001)

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

                # place a red cross on the plot
                plt.plot(j, mean_diff1, 'ro')
                plt.draw()

            prev_compare = "same" if mean_diff1 < difference_threshold and mean_diff2 < difference_threshold else "different"

    i += 1
    # wait 1 second for the next frame
    # time.sleep(.1)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# cv2.waitKey(0)

# plot the mean diff
# plt.plot(plot_diff)
# plt.draw()

# save the plot to a png file
print('saving plot...')
plt.savefig(f"./data/{current_time}/plot.png")  

# plt.show()

cv2.destroyAllWindows()