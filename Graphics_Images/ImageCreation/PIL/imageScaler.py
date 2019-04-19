from PIL import Image
import cv2

def simplify(filename,r,c,newFilename):
    img = Image.open(filename)
    img = img.resize((r,c),Image.LANCZOS)
    img.save(newFilename,quality=100)


def main():
    w, h = int(input("Width: ")),int(input("Height: "))
    cam = cv2.VideoCapture(0)
    cam.set(3,1366) #width
    cam.set(4,768) #height
    ret, frame = cam.read()
    filename = "apture.bmp"
    newFilename = "captureNew.bmp"
    cv2.imwrite(filename,frame)
    simplify(filename,w,h,newFilename)

main()
    
    
