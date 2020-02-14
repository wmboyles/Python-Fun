"""
Finds the average BGR intensity of an image from cv2's camera.
Plots this mean in real time using matplotlib's animation.
"""

import cv2

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib
# For some reason conda uses a non-gui backend by default
matplotlib.use("TkAgg")

# Maximum number of frames to show graphed
MAX = 200
# How often (in ms) should the camera read a new frame?
DELTA = 50
# Range of possible y values. Values outside will not be graphed.
Y_RANGE = [0, 255]
# cv2 Camera object
CAM = cv2.VideoCapture(0)

# matplotlib figure that will be animated
fig = plt.figure()
# an axis in the figure
ax = fig.add_subplot(1, 1, 1)
# X-axis
xs = list(range(0, MAX))
# Y-axis
ys = [0] * MAX
# Set y axis to only graph values in range
ax.set_ylim(Y_RANGE)

# Create a blank line that will be updated
line, = ax.plot(xs, ys)


def animate(i, ys):
    """
    Animation function called by FuncAnimation
    """

    img = CAM.read()[1]
    #cv2.imshow("CAM", img)

    ys.append(img.mean())

    # Limit list size that is displayed
    ys = ys[-MAX:]

    # Update line with new y
    line.set_ydata(ys)

    return line,


if __name__ == '__main__':
    ani = animation.FuncAnimation(
        fig,
        animate,
        fargs=(ys,),
        interval=DELTA,
        blit=True)

    plt.show()

    CAM.release()
    cv2.destroyAllWindows()
