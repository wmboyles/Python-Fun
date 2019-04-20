import cv2  # Computer Vision Library
import numpy as np  # Arrays library
from time import localtime, strftime  # Time library

# Basic Setup
font = cv2.FONT_HERSHEY_SIMPLEX
SIZE = (1280, 720)  # Some resolutions don't work. Confirmed working for (640,480)(standard) and (1280,720)(max)
FRAMERATE = 20.0  # 10-20fps is roughly real time.
WINDOW_NAME = "Motion Decector"

# Camera
cam = cv2.VideoCapture(0)  # camera object
cam.set(cv2.CAP_PROP_FRAME_WIDTH, SIZE[0])  # Set width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, SIZE[1])  # Set height

# Video Recording
vidWriter = cv2.VideoWriter_fourcc(*'XVID')
vidOut = cv2.VideoWriter("out.avi", vidWriter, FRAMERATE, SIZE)  # change dimensions to fit cam

# Motion Threshold: CALIRATE THIS FOR YOUR CAM
WHITE_T = 1500


# Uses 3 images to see if there was motion
def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)  # Difference of 1 and 2
    d2 = cv2.absdiff(t1, t0)  # Difference of 0 and 1
    return cv2.bitwise_and(d1, d2)  # Bitwise and of image differences


def main():
    print("PRESS ESC KEY TO EXIT")
    
    # Get initial 2 images
    t_m = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    while True:
        feed = cam.read()[1]  # Image to show
        t_p = cv2.cvtColor(feed, cv2.COLOR_RGB2GRAY)  # Gets 3rd image for comparison
        img = 32 * np.round(diffImg(t_m, t, t_p) / 32)  # Compares 3 images for motion

        whites = np.count_nonzero(img)  # Number of "differences" between 3 images
        
        # Show time at top-right
        time = strftime("%d/%m/%Y %H:%M:%S", localtime())
        cv2.putText(feed, time, (1050, 20), font, .6, (0, 255, 0), 2, cv2.LINE_AA)

        # Add REC and add to video if there is motion
        if whites > WHITE_T:
            cv2.putText(feed, "REC", (0, 20), font, .8, (0, 0, 255), 2, cv2.LINE_AA)
            vidOut.write(feed)

        # Show live feed w/ REC indicator & time   
        cv2.imshow(WINDOW_NAME, feed)

        # Update to next frame
        t_m, t = t, t_p
        t_p = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

        # Press ESC to end the program
        if cv2.waitKey(10) == 27:
            cam.release()
            vidOut.release()
            cv2.destroyAllWindows()
            break


main()
