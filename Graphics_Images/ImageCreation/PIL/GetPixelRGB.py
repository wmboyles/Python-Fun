from PIL import Image

filename = 'img1.bmp'


def GetPixelRGB(x, y):
    im = Image.open(filename)
    pix = im.load()
    return pix[x, y]


print(GetPixelRGB(int(input("x: ")), int(input("y: "))))
input("Press ENTER...")
