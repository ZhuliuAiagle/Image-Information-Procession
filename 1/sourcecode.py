#import essential module
from PIL import Image, ImageDraw
#import math module in need of funtcion atan() and abs()
import math
#Calculate deltaH with fomula
def deltaH(im, i, j):
    zs = im.getpixel((i - 1, j - 1))
    ys = im.getpixel((i - 1, j + 1))
    z = im.getpixel((i, j - 1))
    y = im.getpixel((i, j + 1))
    zx = im.getpixel((i + 1, j - 1))
    yx = im.getpixel((i + 1, j + 1))
    result = (zs + z + zx)*(-1) + (ys + y + yx)*1
    return result
#Calculate deltaV with fomula
def deltaV(im, i, j):
    zs = im.getpixel((i - 1, j - 1))
    s = im.getpixel((i - 1, j))
    ys = im.getpixel((i - 1, j + 1))
    zx = im.getpixel((i + 1, j - 1))
    x = im.getpixel((i + 1, j))
    yx = im.getpixel((i + 1, j + 1))
    result = (zs + s + ys) * 1 + (zx + x + yx) * (-1)
    return result
#Calculate deltaG
def deltaG(im, i, j):
    return int(abs(deltaH(im, i, j)) + abs(deltaV(im, i, j)) / 2)
#Calculate direction(in radian)
def certa(im, i, j):
    return math.atan(deltaV(im, i, j) / deltaH(im, i, j)) + math.pi / 2
#main program
#list used to store the module value,since the grey value can't be changed right now
li = []
str = input("please input the name of file(local file only!): ")
if(str != "girl.bmp" and str != "apple.bmp"):
    print("Ooops! There isn't such file! STOP!!")
else:
    print("Please wait...")
    im = Image.open(str)
    #convert to grey-style image
    im = im.convert("L")
    draw = ImageDraw.Draw(im)
    #store deltaG value
    print("Reading the image...", end="")
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if(i > 0 and i < im.size[0] - 1 and j > 0 and j < im.size[1] - 1):
                li.append(deltaG(im, i, j))
    print("Finish")
    k = 0
    #Change the grey value of every point
    print("Processing the image...", end="")
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if(i > 0 and i < im.size[0] - 1 and j > 0 and j < im.size[1] - 1):
                draw.point((i, j), fill = li[k])
                k += 1
    print("Finish")
    #save image
    im.save("result.bmp")
    print("______ALL DONE______")
    im.show()


