__author__ = 'coffeephantom'

import urllib
import urllib2

def get_url_src(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html
