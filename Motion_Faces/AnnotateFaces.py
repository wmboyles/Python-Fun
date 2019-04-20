import cv2
import numpy as np

SIZE = (1366, 768)
FRAMERATE = 10.0
WINDOW_NAME = "Face Detection"

# Camera Object
cam = cv2.VideoCapture(0)

# face_identifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
if face_cascade.empty():
  raise IOError('Unable to load the face cascade classifier xml file')

# smile identifier
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
if smile_cascade.empty():
  raise IOError('Unable to load the smile cascade classifier xml file')

# eye identifier
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
if eye_cascade.empty():
  raise IOError('Unable to load the eye cascade classifier xml file')


# Find faces in images, add a rectangle, and return the image with the faces identified
def findFaces(feed):
    # get a grayscale image
    gray = cv2.cvtColor(feed, cv2.COLOR_BGR2GRAY)

    # Find faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # put green rectangles on image and find the dimension of all faces
    for (x, y, w, h) in faces:
        cv2.rectangle(feed, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = feed[y:y + h, x:x + w]
        
        eyes = eye_cascade.detectMultiScale(
            cropped,
            scaleFactor=1.1,
            minNeighbors=20
        )
        # put red rectangles on eyes
        for (x, y, w, h) in eyes:
            cv2.rectangle(cropped, (x, y), (x + w, y + h), (0, 0, 255), 2)

        smiles = smile_cascade.detectMultiScale(
            cropped,
            scaleFactor=1.6,
            minNeighbors=30
        )
        # put blue rectangles on smiles
        for (x, y, w, h) in smiles:
            cv2.rectangle(cropped, (x + 5, y + 5), (x + w - 5, y + h - 5), (255, 0, 0), 2)
        
    # return the image with the rectangles
    return feed


# Create a camera feed and display the result
def main():
    print("Press ESC to End")

    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    
    while True:
        cv2.imshow(WINDOW_NAME, findFaces(cam.read()[1]))

        # Press ESC key to end the program
        if cv2.waitKey(10) == 27:
            cam.release()
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
    
