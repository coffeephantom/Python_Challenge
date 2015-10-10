#-*-coding: utf-8-*-

__author__ = 'Administrator'


import Image
import ImageDraw

img = Image.open('cave.jpg')
img_copy = Image.open('cave.jpg')
height, width = img.size
print height, width
for i in range(height):
    for j in range(width):
        if i % 2 != 0 or j % 2 !=0:
            img_copy.putpixel([i, j],(0,0,0))

img_copy.save('cave_copy.jpg')
