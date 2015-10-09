import string

__author__ = 'coffeephantom'

with open('mess.txt') as f:
    data = f.read()
# to find rare character
def find_rare_char(text):
    s = filter(lambda x:x in string.letters, text)
    return s

print find_rare_char(data)





def std_solution(text):
    s = ''.join([line.rstrip() for line in text])
    occ = {}

    for c in s:
        occ[c] = occ.get(c, 0) + 1
        avgoc =len (s)/len(occ)
    return ''.join([c for c in s if occ[c] < avgoc])

print std_solution(data)

