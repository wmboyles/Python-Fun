import cv2

cam = cv2.VideoCapture(0)
while True:
    ret_val, img = cam.read()
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) == 27:  # escape key
        break

cv2.destroyAllWindows()
cam.release()
