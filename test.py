import matplotlib.pyplot as plt

current_time = 234
fps = 23
difference_threshold = 2.5

# save the fps, threshold, and file name to a csv file
with open(f"./data.csv", "w") as f:
    f.write("fps, threshold, file_name\n")
    f.write(f"{fps}, {difference_threshold}, {current_time}\n")