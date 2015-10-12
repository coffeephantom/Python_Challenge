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

# ����ͼƬ�Ľ�
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y, z = -1, 0, 0

# ������ͼ�е����е�
for i in range(200):
    d = dirs[i % 4]
    print d
    for j in range(100-(i + 1)/2):
        x += d[0]
        y += d[1]
        print (x,y)

       # ��ԭͼ�е����ص���Ƶ���ͼ�У�ԭͼ��������ֻ��0,1
        img_new.putpixel((x,y), img.getpixel((z,0)))
        z += 1

img_new.save('sprial_wire.png')
