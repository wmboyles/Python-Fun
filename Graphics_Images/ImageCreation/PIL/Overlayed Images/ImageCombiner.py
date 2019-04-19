from PIL import Image
from math import sqrt



def resizeSave(filename,size):
    img = Image.open(filename)
    imgOut = img.resize(size)
    imgOut.save(filename)
    imgOut.show()



def rotateSave(filename,angle):
    img = Image.open(filename)
    imgOut = img.rotate(angle)
    imgOut.save(filename)
    imgOut.show()



def maxOverlayCombine(filename1,filename2,outFilename):
    img1 = Image.open(filename1)
    pix1 = img1.load() #It's a LOT faster to load image within function 
    h1, w1 = img1.size

    img2 = Image.open(filename2)
    pix2 = img2.load()
    h2, w2 = img2.size # (width,height)

    imageOut = Image.new('RGB',(min(w1,w2),min(h1,h2))) #Only overlay overlapping part of images
    outPixels = imageOut.load() #To place in pixels

    for x in range(imageOut.width):
        for y in range(imageOut.height):
            color1, color2 = pix1[x,y], pix2[x,y] #(Red, Green, Blue, Gamma)
            outPixels[x,y] = color1 if color1>=color2 else color2

    imageOut.save(outFilename) #Save
    imageOut.show() #Display Result



def minOverlayCombine(filename1,filename2,outFilename):
    img1 = Image.open(filename1)
    pix1 = img1.load() #It's a LOT faster to load image within function 
    h1, w1 = img1.size

    img2 = Image.open(filename2)
    pix2 = img2.load()
    h2, w2 = img2.size # (width,height)

    imageOut = Image.new('RGB',(min(w1,w2),min(h1,h2))) #Only overlay overlapping part of images
    outPixels = imageOut.load() #To place in pixels

    for x in range(imageOut.width):
        for y in range(imageOut.height):
            color1, color2 = pix1[x,y], pix2[x,y] #(Red, Green, Blue, Gamma)
            outPixels[x,y] = color1 if color1<=color2 else color2

    imageOut.save(outFilename) #Save
    imageOut.show() #Display Result

    
    
def avgCombine(filename1, filename2, outFilename): #Can be .bmp or .png that are RGB
    img1 = Image.open(filename1)
    pix1 = img1.load() #It's a LOT faster to load image within function 
    h1, w1 = img1.size

    img2 = Image.open(filename2)
    pix2 = img2.load()
    h2, w2 = img2.size # (width,height)

    imageOut = Image.new('RGB',(min(w1,w2),min(h1,h2))) #Only overlay overlapping part of images
    outPixels = imageOut.load() #To place in pixels
    
    for x in range(imageOut.width):
        for y in range(imageOut.height):
            color1, color2 = pix1[x,y], pix2[x,y] #(Red, Green, Blue, Gamma)
            outPixels[x,y] = ( int((color1[0]+color2[0])*1/sqrt(2)), int((color1[1]+color2[1])*1/sqrt(2)), int((color1[2]+color2[2])*1/sqrt(2)))

    imageOut.save(outFilename) #Save
    imageOut.show() #Display Result



def sumCombine(filename1,filename2,outFilename):
    img1 = Image.open(filename1)
    pix1 = img1.load() #It's a LOT faster to load image within function 
    h1, w1 = img1.size

    img2 = Image.open(filename2)
    pix2 = img2.load()
    h2, w2 = img2.size # (width,height)

    imageOut = Image.new('RGB',(min(w1,w2),min(h1,h2))) #Only overlay overlapping part of images
    outPixels = imageOut.load() #To place in pixels
    
    for x in range(imageOut.width):
        for y in range(imageOut.height):
            color1, color2 = pix1[x,y], pix2[x,y] #(Red, Green, Blue, Gamma)
            outPixels[x,y] = ((color1[0]+color2[0]), (color1[1]+color2[1]), (color1[2]+color2[2]))

    imageOut.save(outFilename) #Save
    imageOut.show() #Display Result



def geoMeanCombine(filename1,filename2,outFilename):
    img1 = Image.open(filename1)
    pix1 = img1.load() #It's a LOT faster to load image within function 
    h1, w1 = img1.size

    img2 = Image.open(filename2)
    pix2 = img2.load()
    h2, w2 = img2.size # (width,height)

    imageOut = Image.new('RGB',(min(w1,w2),min(h1,h2))) #Only overlay overlapping part of images
    outPixels = imageOut.load() #To place in pixels
    
    for x in range(imageOut.width):
        for y in range(imageOut.height):
            color1, color2 = pix1[x,y], pix2[x,y] #(Red, Green, Blue, Gamma)
            outPixels[x,y] = (int(sqrt(color1[0]*color2[0])), int(sqrt(color1[1]*color2[1])), int(sqrt(color1[2]*color2[2])))

    imageOut.save(outFilename) #Save
    imageOut.show() #Display Result
