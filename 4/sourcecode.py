#import Image, ImageDraw. ImageDraw is used to change the gray value
from PIL import Image, ImageDraw
#function Operation(): it is used to calculate the result of image equalization formula
#-------------------------------------------------------------------------------
def Operation(cdf, cdfmin, M, N, L):
    return round((cdf - cdfmin)/(M * N - cdfmin) * (L - 1))
#-------------------------------------------------------------------------------
#main program
#open image
str = input("please input the name of file(local file only!): ")
if(str != "girl.bmp" and str != "apple.bmp"):
    print("Ooops! There isn't such file! STOP!!")
else:
    print("Please wait...")
    im = Image.open(str)
    #convert the mode of image from RGB into L, since the given instances are RGB-based image.
    im = im.convert("L")
    #create an empty list to store the occuring time of every gray value
    li = []
    #distribute 256 spaces. position i will store the number of pixels whose gray values are equal to i
    for i in range(0,256):
        li.append(0)
    #get width and height(M&N)with a tuple
    (width, height) = im.size
    #draw is an oval, through which we can modify the image content
    draw = ImageDraw.Draw(im)
    #Traverse the image matrix(O(N^2)), calculate the frequency of each grayscale value and stored in the list
    print("Reading the image...", end = "")
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            gray = im.getpixel((j,i))
            li[gray] += 1
    #calculate the cumulative distributions by adding all the frequencies one by one
    for i in range(1, 256):
        li[i] = li[i] + li[i - 1]
    #find the smaller cumulative distribution except for zero
    ri = 0
    while li[ri] == 0:
        ri += 1
    cdfmin = li[ri]
    print("Finish")
    #Traverse the image matrix and change the gray value with function draw.point() one by one
    #it may take times
    print("Processing the image...",end = "")
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            gray = im.getpixel((j, i))
            draw.point((j, i),fill = Operation(li[gray], cdfmin, width, height, 256))
    print("Finish")
    #save the image
    im.save("result.bmp")
    print("______ALL DONE______")
    im.show()






