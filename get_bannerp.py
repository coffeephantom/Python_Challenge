__author__ = 'Administrator'
import urllib
import urllib2

response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
data = response.read()


with open('banner.p', 'w') as f:
    f.write(data)