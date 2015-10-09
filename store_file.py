__author__ = 'coffeephantom'

from get_url_src import get_url_src
import re
def store_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)
    f.close()
text = get_url_src('http://www.pythonchallenge.com/pc/def/equality.html')
text_list = text.split('\n')
index = text_list.index('<!--')
new_list = text_list[index+1:(len(text_list)-1)]
new_text = '\n'.join(new_list)

store_file('mess2.txt', new_text)