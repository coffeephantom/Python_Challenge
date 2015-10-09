__author__ = 'coffeephantom'

import os
import re

search = re.compile("(\d*)$")
str = []

dir_path = '/Users/coffeephantom/Downloads/channel/'

file_name = '90052'

extend_name = '.txt'

comment = "#"

for i in range(0, 913):
    with open('%s%s%s' %(dir_path, file_name, extend_name)) as f:
        content = f.read()
        print content

        match = search.findall(content)
        print match

        if not match[0]:
            file_name = match[0]
        else:
            break

file_list = os.listdir(dir_path)
print file_list


