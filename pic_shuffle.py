__author__ = 'Administrator'# refer to http://garethrees.org/2007/05/07/python-challenge/with open('evil2.gfx','rb') as f:    content = f.read()print len(content)print content[:25]print type(content)file_types = ['jpg', 'png', 'gif', 'png', 'jpg']for i in range(5):    with open("%s%d.%s" % ('evil2_', i, file_types[i]), 'wb') as f:        f.write(content[i::5])