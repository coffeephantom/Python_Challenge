__author__ = 'coffeephantom'

import urllib
import urllib2
import re


# data = {}
number = '12345'
count = 0
# url_ori = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
search = re.compile('(\d*)$')
search_html = re.compile('\.html$')

while count <= 400:
    print '%s' % number
    response = urllib2.urlopen("%s%s" %(url, number))
    data = response.read()
    print data

    if search_html.findall(data):
        break

    match = search.findall(data)
    if match:
        number = match[0]
    else:
        number = str(int(number)/2)
    count += 1
    print count