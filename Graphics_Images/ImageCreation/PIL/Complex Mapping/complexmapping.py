from PIL import Image, ImageDraw
import math


def CxFunct(a, b):  # input a,b is z=a+bi
    z = complex(a, b)
    try:
        return 10000000000*math.e**(.1/z)
    except ZeroDivisionError:
        return 0


def main(screenL, screenW): #i.e. 1366, 768 or 1920, 1080
    filename = 'img1.bmp'
    image = Image.new('RGB', (screenL, screenW))
    size = width, height = image.size
    pixels = image.load()

    delta = 1 #Positive Integer

    #(0,0) at center of image
    for a in range(1-screenL//2, screenL//2, delta):
        for b in range(1-screenW//2, screenW//2, delta):
            
            # if((int(a/10)==a/10 or int(b/10)==b/10)): # plot a grid
            c = CxFunct(a,b) #result of complex fuction
            if((c.real + screenL//2) < screenL and int(c.real + screenL//2) >= 0 and int(screenW//2 - c.imag) < screenW and int(screenW//2 - c.imag) >= 0):
                pixels[int(c.real + screenL//2), int(screenW//2 - c.imag)] = (255, 255, 255)  # Plot

    image.save(filename)
    

main(1000,1000)
