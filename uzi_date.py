#-*-coding:utf-8—*-
__author__ = 'Administrator'

import re
from datetime import *

pattern = re.compile(r'1\d{2}6$')
list_year = range(1000, 2000)
list_new = []
for i in list_year:
    if pattern.match(str(i)):
        list_new.append(i)

def isLeap(year):
     if year % 400 == 0:
         return True
     elif year % 4 == 0:
         if year % 100 == 0:
             return False
         else:
             return True
     else:
         return False

list_leap = filter(isLeap, list_new)

result = []
for i in list_leap:
    if datetime.weekday(date(i, 1, 1))==3:
        print i

# next link: http://www.pythonchallenge.com/pc/return/mozart.html
