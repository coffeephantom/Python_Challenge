__author__ = 'Administrator'
import pickle

with open('banner.p') as f:
    output = pickle.load(f)
    for each in output:
        print ''.join(i[0] * i[1] for i in each)
