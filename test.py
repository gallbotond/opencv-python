import matplotlib.pyplot as plt

# Create an empty plot
fig, ax = plt.subplots()

# Initialize the plot with some data
x = [0]
y = [0]
line, = ax.plot(x, y)

# Update the plot in a for loop
for i in range(0, 100):
    x.append(i)
    y.append(i**2)
    line.set_data(x, y)
    ax.relim()
    # ax.autoscale_view()
    plt.draw()
    plt.pause(0.1)