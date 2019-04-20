import cv2
import numpy as np

cam = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

img1 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
img2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
img3 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

while True:
    feed = cam.read()[1]
    
    d1 = cv2.absdiff(img1, img2)
    d2 = cv2.absdiff(img2, img3)

    imgB = cv2.bitwise_and(d1, d2)
    imgM = 32 * np.round(imgB / 32)

    whites = np.count_nonzero(imgM)

    if whites >= 200:
        cv2.circle(feed, (10, 10), 7, (0, 0, 255), 14)
    else:
        cv2.circle(feed, (10, 10), 7, (0, 255, 0), 14)
        
    cv2.imshow("M", feed)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cam.release()
        break

    img1 = img2
    img2 = img3
    img3 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
