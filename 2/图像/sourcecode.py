# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image
import math
#=---------------------------------------------------------------
#Gauss function that used to generate gauss martix
def gauss(fc):
    li = []
    for i in range(0, 7):
        li.append([0,0,0,0,0,0,0])
    add2 = 0
    for i in range(0, 7):
        for j in range(0, 7):
            li[i][j] = 1/(2*math.pi*fc*fc)*math.exp(-((i - 3)**2 + (j - 3)**2)/(2*fc*fc))
            add2 = add2 + li[i][j]
    for i in range(0, 7):
        for j in range(0, 7):
            li[i][j] /= add2
    return li
#im:a temporary variable  to store the image got from a certain file
#im1:store result 1
#im2:store result 2
#in2:store the final result
im = Image.open("flower.jpg")
im = im.convert('L')
im1 = Image.new('L',im.size, 0)
im2 = Image.new('L',im.size, 0)
im3 = Image.new('L',im.size, 0)
#set variance to 1
fc = 1
#get 7*7 gauss martix
li = gauss(fc)
#temporary list to store the  output gray value
store = []
#calculate the gray value and temprorily store them into the list
for i in range(3, im.size[0] - 3):
    for j in range(3, im.size[1] - 3):
        temp = 0;
        for k in range(0, 7):
            for f in range(0, 7):
                temp += li[k][f] * im.getpixel((i - 3 + k, j - 3 + f))
        store.append(temp)
#change the gray value of the image one by one
k = 0
for i in range(3, im.size[0] - 3):
    for j in range(3, im.size[1] - 3):
        im.putpixel((i, j), round(store[k]))  
        k += 1
im.save("re1.bmp")
#reset the variance and clear storage list
#the following are all the same as we have mentioned above
fc = 1.6
li = gauss(fc)
store = []
for i in range(3, im.size[0] - 3):
    for j in range(3, im.size[1] - 3):
        temp = 0;
        for k in range(0, 7):
            for f in range(0, 7):
                temp += li[k][f] * im.getpixel((i - 3 + k, j - 3 + f))
        store.append(temp)
   
k = 0
for i in range(3, im.size[0] - 3):
    for j in range(3, im.size[1] - 3):
        im.putpixel((i, j), round(store[k]))  
        k += 1
im.save("re2.bmp")
#subtract the two image and get the final result
im1 = Image.open("re1.bmp")
im2 = Image.open("re2.bmp")
for i in range(0, im.size[0]):
    for j in range(0, im.size[1]):
        im3.putpixel((i, j), 255 - (im1.getpixel((i, j)) - im2.getpixel((i, j))) )
im3.save("hahaha.bmp")

    
