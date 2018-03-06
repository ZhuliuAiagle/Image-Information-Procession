from PIL import Image, ImageDraw
im1 = Image.open("1-1.jpg")
im2 = Image.open("1-2.jpg")
im3 = Image.open("1-masking.jpg")
im3 = im3.convert('L')
print(im1.size)
for i in range(im2.size[0]):
    for j in range(im2.size[1]):
        if(i + 22 >= im1.size[0] or j + 6 >= im1.size[1]):
            break
        tup1 = im1.getpixel((i + 22, j + 6))
        tup2 = im2.getpixel((i, j))
        tup3 = [0, 0, 0]
        if(im3.getpixel((i, j)) == 255):
            tup3[0] = round(tup1[0] * 0.5 + tup2[0] * 0.5)
            tup3[1] = round(tup1[1] * 0.5 + tup2[1] * 0.5)
            tup3[2] = round(tup1[2] * 0.5 + tup2[2] * 0.5)
            im1.putpixel((i + 22, j + 6),tuple(tup3))
        else:
            pass
        if (i + 22 >= im1.size[0]):
            break
    im1.save('result_alpha_beta1.bmp')

im1 = Image.open("2-1.jpg")
im2 = Image.open("2-2.jpg")
im3 = Image.open("2-masking.jpg")
im3 = im3.convert('L')
print(im1.size)
for i in range(im2.size[0]):
    for j in range(im2.size[1]):
        if(i + 31 >= im1.size[0] or j + 236 >= im1.size[1]):
            break
        tup1 = im1.getpixel((i + 31, j + 236))
        tup2 = im2.getpixel((i, j))
        tup3 = [0, 0, 0]
        if(im3.getpixel((i, j)) == 255):
            tup3[0] = round(tup1[0] * 0.5 + tup2[0] * 0.5)
            tup3[1] = round(tup1[1] * 0.5 + tup2[1] * 0.5)
            tup3[2] = round(tup1[2] * 0.5 + tup2[2] * 0.5)
            im1.putpixel((i + 31, j + 236),tuple(tup3))
        else:
            pass
        if (i + 31 >= im1.size[0]):
            break
    im1.save('result_alpha_beta2.bmp')

im1 = Image.open("3-1.jpg")
im2 = Image.open("3-2.jpg")
im3 = Image.open("3-masking.jpg")
im3 = im3.convert('L')
print(im1.size)
for i in range(im2.size[0]):
    for j in range(im2.size[1]):
        if(i + 208 >= im1.size[0] or j + 206 >= im1.size[1]):
            break
        tup1 = im1.getpixel((i + 208, j + 206))
        tup2 = im2.getpixel((i, j))
        tup3 = [0, 0, 0]
        if(im3.getpixel((i, j)) == 255):
            tup3[0] = round(tup1[0] * 0.5 + tup2[0] * 0.5)
            tup3[1] = round(tup1[1] * 0.5 + tup2[1] * 0.5)
            tup3[2] = round(tup1[2] * 0.5 + tup2[2] * 0.5)
            im1.putpixel((i + 208, j + 206),tuple(tup3))
        else:
            pass
        if (i +208 >= im1.size[0]):
            break
    im1.save('result_alpha_beta3.bmp')