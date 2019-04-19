from PIL import Image, ImageDraw
import math

def CxFunct(a,b): #input a,b is z=a+bi
    z = complex(a,b)
    return .0000000001*math.e**z
def main():
    filename = 'img1.bmp'
    image = Image.new('RGB',(768,768))
    size = width,height = image.size
    pixels = image.load()

    a=-384
    b=-384

    for a in range(-682,683,1):
        for b in range(-382,384,1):
            
            #if((int(a/10)==a/10 or int(b/10)==b/10)): # plot a grid
            if(int(CxFunct(a,b).real+683)<768 and int(CxFunct(a,b).real+683)>=0 and int(384-CxFunct(a,b).imag)<768 and int(384-CxFunct(a,b).imag)>=0):
                pixels[int(CxFunct(a,b).real+683),int(384-CxFunct(a,b).imag)] = (255,255,255) #Plot

        image.save(filename)
    

main()
