__author__ = 'Administrator'


import Image


img = Image.open('oxygen.png', 'r')
size = img.size

print size

data = [img.getpixel((i,j)) for  i in range(0,609) for j in range(43,53)]
print data

row = [chr(img.getpixel((i, 43))[0]) for i in range(0, 609, 7)]
print "".join(row)

print "".join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))