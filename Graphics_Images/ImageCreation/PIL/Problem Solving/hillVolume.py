from PIL import Image
from random import randint

def drawHill(hill,filename):
    hillL, maxH = len(hill), max(hill)+1
    image = Image.new('RGB',(hillL,maxH))
    pix = image.load()
    
    for y in range(maxH):
        for x in range(hillL):
            if hill[x]>=maxH-y: pix[x,y] = (139,69,19) #brown
            else: pix[x,y] = (0,191,255) #blue

    image.save(filename)


def getColVol(x,y,filename):
    #One liner w/o coloring
    #return sum(pix[x,depth]==(0,191,255) for depth in range(y+1,image.size[1]))
    image = Image.open(filename)
    pix = image.load()
    w,h = image.size
    colVol=0
    for depth in range(y+1,h):
        if pix[x,depth]==(0,191,255):
            pix[x,depth]=(0,0,205) #dark blue
            colVol+=1
        else:
            image.save(filename)
            return colVol


def getSectorVol(startX,endX,lineHeight,filename): return sum(getColVol(x,lineHeight,filename) for x in range(startX,endX+1))


def getVol(hill,filename):
    volume, startX = 0, 0
    w, h = len(hill), max(hill)+1
    currentLineHeight = h-(hill[startX]+1)
    
    while startX<w:
        for x in range(startX+1,w,1):
            if x==w-1: currentLineHeight+=1 #lower down the hill/image
            
            if hill[x]+1 >= h-currentLineHeight:
                volume += getSectorVol(startX,x,currentLineHeight,filename)
                if x==w-1: return volume
                else:
                    startX=x
                    currentLineHeight = h-(hill[x]+1)
                    x=w

                    
#Makes image of hill, calculates volume from image, and fills hill with water
def main():
    filename = 'hill.bmp'
    
    hill = [4,2,4,1,5,3,16,6,17,19,4,13,5,3,10,10,13,6,2,1,5,15,13,19,16,9,13,1,7,18,20,13,9,7,2,10,8,18,4,7,5,8,10,13,7,18,19,2,19,8,10,10,17,6,6,20,20,11,10,11,13,9,7,1,10,5,12,16,10,7,15,13,12,10,1,1,4,2,16,10,20,17,11,19,19,20,9,10,17,9,18,8,10,18,8,19,16,17,3,1]
    #hill = []
    #for i in range(100): hill.append(i+1)

    print(main2(hill))
    drawHill(hill,filename)
    return getVol(hill,filename)


#Uses an algorithm to find the volume w/o any images -- faster way (long one-liner)
def main2(hill): return sum(max(0,min(max(hill[:i]),max(hill[i+1:]))-hill[i]) for i in range(1,len(hill)-1))
