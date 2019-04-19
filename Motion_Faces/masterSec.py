import cv2
import numpy as np
from time import localtime, strftime, sleep
from os import makedirs, execv, fsync
from sys import argv, stdout

# Setup stuff that defines how the video will look.
font = cv2.FONT_HERSHEY_SIMPLEX
SIZE = (640,480)
FRAMERATE = 20.0
WINDOW_NAME = "Security Program 0.2.2.1"
date =  strftime("%d-%m-%y",localtime()) #Day-Month-Year formatting

#Camera object
cam = cv2.VideoCapture(0)
vidWriter = cv2.VideoWriter_fourcc(*'XVID')
vidOut = None #Tells how and where to write the video. Will be updated when the savd location is created.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#White = change = motion threshold -- will be calibrated and managed automatically.
WHITE_T = 0

# The number of continuous frames that motion can detected without faces before the motion threshold is increased. Change as needed to suit the room.
FRAME_LIMIT = 200

# A measure of how much motion has happened recently.
contFrames = 0
CONT_FRAMES_MAX = 2*FRAME_LIMIT
CONT_FRAMES_MIN = -2*FRAME_LIMIT

# The number
FACE_LIMIT = 20
# The number of continious frames a face has been detected
contFaces = 0

WHITE_T_MIN = 100 #Minimum white threshold
WHITE_T_MAX = 5000 #Maximum white threshold 


def calibrate():
    global WHITE_T
    sleep(3)
    print("Calibrating...")
    WHITE_T = max(newWhiteT(),100)
    print("Done.")


def checkWhiteAdjust():
    global WHITE_T, WHITE_T_MIN, WHITE_T_MAX, contFrames, contFaces, FACE_LIMIT

    #If there is noisy (non) motion and no faces
    if WHITE_T!=WHITE_T_MAX and contFrames>=FRAME_LIMIT and contFaces<FACE_LIMIT:
        if WHITE_T<WHITE_T_MAX: WHITE_T += 250
        contFrames = 0

    #If White_t is too high...
    elif WHITE_T!=WHITE_T_MIN and contFrames<=-1*FRAME_LIMIT  and contFaces<FACE_LIMIT: #The camera isn't sensitive enough
        if WHITE_T>=2*WHITE_T_MIN: WHITE_T -= 100
        contFrames=0


#gets 100 frames and gets 75th %-tile whites
def newWhiteT():
    whiteCounts = []
    
    #Get initial 3 images
    t_m, t, t_p = threeInitial()
    
    for i in range(99): #get 99 more updated frames
        feed = cam.read()[1]
        
        #Image to look for black pixels
        img = diffImg(t_m,t,t_p)

        #Number of white pixels
        whites = np.count_nonzero(img)
        whiteCounts.append(whites)

        #Update to next frame
        t_m, t, t_p = updateFrame(t_m,t,t_p)

    Q3White = int(np.percentile(whiteCounts,75)) #get 75th percentile of white values
    return Q3White


# Makes a folder for today if applicable
def checkInitial():
    global date, vidOut #Refernece the global variable

    vidOut = cv2.VideoWriter("Faces\\" + date + "\\" + date + ".avi", vidWriter, FRAMERATE, SIZE) #Saved in Faces folder as the date
    
    try: makedirs("Faces\\"+date) #trys to make a file for the date
    except OSError: pass #else does nothing


# If the day changes, end today's video and start a new one -- NOT WORKING YET
def checkNewDate():
    global date, vidOut
    
    if date!=strftime("%d-%m-%y",localtime()): #If the date has changed...
        date = strftime("%d-%m-%y",localtime()) #update the date
        vidOut = cv2.VideoWriter("Faces\\" + date + ".avi", vidWriter, FRAMERATE, SIZE) #Saved in Faces folder as the date
        cam.release() #save today's images
        vidOut.release() #save today's video
        #cv2.destroyAllWindows() #close all of today's windows
        #restart srcipt

#detect faces in image
def findFaces(feed): 
    global contFaces
    
    checkNewDate()
    
    nowS = strftime("%H-%M-%S",localtime()) #Hour-Min-Sec
    nowD = strftime("%H:%M:%S",localtime()) #Hour:Min:Sec
    
    gray = cv2.cvtColor(feed,cv2.COLOR_BGR2GRAY)

    #Finds faces within parameters
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40,40),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(feed,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imwrite("Faces\\"+date+"\\"+nowS+".jpg",feed) #Saves color image of face w/ rectangle
        print("Face: "+nowD)

    if len(faces)!=0 and contFaces < FACE_LIMIT: contFaces+=1
    elif contFaces > -1*FACE_LIMIT: contFaces-=1
    
    return feed

  
# Defermines the amount of change (motion) between frames of an image
def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1) #Difference of 1 and 2
    d2 = cv2.absdiff(t1, t0) #Difference of 0 and 1
    f = cv2.bitwise_and(d1, d2) #Bitwise and of differences
    return 32*np.round(f/32)


# Adds text to the video feed: The motion value & threshold and date.
def putTexts(feed, whites):
    
    #Show time at top-right
    time = strftime("%d/%m/%Y %H:%M:%S", localtime())
    cv2.putText(feed, time, (420,20), font, .6, (0,255,0), 2, cv2.LINE_AA)

    #Put current motion values in bottom left
    cv2.putText(feed, "Motion: "+str(whites)+"/"+str(WHITE_T), (0,470), font, .5, (0,255,0), 2, cv2.LINE_AA)

    #Put recent motion number (contFrames) in the bottom middle
    cv2.putText(feed, "Recent Motion: "+str(contFrames)+"/"+str(FRAME_LIMIT), (0,50), font, .5, (0,255,0), 2, cv2.LINE_AA)
    
    #Put recent faces number (contFaces) in the bottom middle
    cv2.putText(feed, "Recent Faces: "+str(contFaces)+"/"+str(FACE_LIMIT), (450,50), font, .5, (0,255,0), 2, cv2.LINE_AA)

    return feed


# Gets three inital frams of the video feed
def threeInitial():
    a = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    b = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    c = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    return [a,b,c]


# Moves the video frames in sequence by 1
def updateFrame(t_m,t,t_p):
    a = t
    b = t_p
    c = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    return [a,b,c]


#Runs the program
def main():
    #Setup Stuff
    global contFrames, WHITE_T


    checkInitial() #Make initial daily folder if it deosn't already exist
    calibrate() #Set the motion threshold
    
    #Get initial 3 images
    t_m, t, t_p = threeInitial()

    #Actual Monitoring Begins

    while True:
        feed = cam.read()[1] #one image frame
        
        #find the white pixels (motion) in the frames
        img = diffImg(t_m,t,t_p)
        whites = np.count_nonzero(img)

        #Add info to live image view
        feed = putTexts(feed,whites)
        
        if whites>=WHITE_T: #If there is motion...
            if contFrames < CONT_FRAMES_MAX: contFrames+=1
            checkWhiteAdjust() #Adjust WHITE_T if needed
            cv2.putText(feed,"REC",(0,20),font,.8,(0,0,255),2,cv2.LINE_AA)
            feed = findFaces(feed) #ADD RECTANGLES to any faces
            vidOut.write(feed) #Write pic w/ movement to video file

        elif contFrames > CONT_FRAMES_MIN: contFrames-=1        
        
        #Show live feed w/ REC, time, and faces
        cv2.imshow(WINDOW_NAME, feed)

        #Update to next frame
        t_m, t, t_p = updateFrame(t_m,t,t_p)

        #Press ESC key to end the program
        if cv2.waitKey(10)==27:
            cam.release()
            vidOut.release()
            cv2.destroyAllWindows()
            break

if __name__== '__main__':
    main()
