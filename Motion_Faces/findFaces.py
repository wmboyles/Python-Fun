from time import localtime, strftime, sleep
import cv2
from msvcrt import getch  # Does Pi have this?
from os import makedirs  # Does Pi have this?

# different file location for Pi
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)  # camera object

font = cv2.FONT_HERSHEY_SIMPLEX

date = strftime("%d-%m-%y", localtime())  # Day-Month-Year
CHECK_FREQUENCY = 1  # Number of seconds between checks for faces (>=1.0)


# Below finds faces and saves the image containing faces
def findFaces():
    now = strftime("%H-%M-%S", localtime())  # Hour-Min-Sec
    
    ret, frame = cam.read()  # gets camera feed
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converts to grayscale

    # Finds faces within parameters (might be differnt for Pi and circumstances)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draws rectangle around face
        time = strftime("%d/%m/%Y %H:%M:%S", localtime())
        cv2.putText(frame, time, (420, 20), font, .6, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imwrite("Faces\\" + date + "\\" + now + ".jpg", frame)  # Saves color image of face w/ rectangle
        print("Found Face at " + now)


# Below creates a folder for faces each day if the folders doesn't already exist
def checkFolders():
    global date
    if date != strftime("%d-%m-%y", localtime()):
        date = strftime("%d-%m-%y", localtime())
        print("NEW DAY: " + date)
        try:
            makedirs("Faces\\" + date)
            print("Today's Directory Created")
        except OSError:
            print("Directory already made")
            pass


def dailyFolder1():
    global date
    try:
        makedirs("Faces\\" + date)
    except OSError:
        pass

    
def main():
    while True:
        checkFolders()
        findFaces()
        sleep(CHECK_FREQUENCY)
        
    cam.release()
    cv2.destroyAllWindows()


main()
