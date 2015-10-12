#-*-coding:utf-8-*-
__author__ = 'Administrator'

import Image

img = Image.open('wire.png')
pixels = img.load()

img_new = Image.new(img.mode,(100, 100))
width,height = img.size
print "height = %s" % (height)
print "width = %s" % (width)
print "mode = %s" % (img.mode)

# 代表图片四角
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y, z = -1, 0, 0

# 遍历新图中的所有点
for i in range(200):
    d = dirs[i % 4]
    print d
    for j in range(100-(i + 1)/2):
        x += d[0]
        y += d[1]
        print (x,y)

       # 将原图中的像素点绘制到新图中，原图的纵坐标只有0,1
        img_new.putpixel((x,y), img.getpixel((z,0)))
        z += 1

img_new.save('sprial_wire.png')
