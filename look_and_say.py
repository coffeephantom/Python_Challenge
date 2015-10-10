#-*-coding: utf-8-*-
__author__ = 'Administrator'


# oeis.org中的python代码

def look_and_say(n):
    seq = [1] + [None] * (n-1)
    def say(s):
        # 分配整个序列空间

        # 初始化
        acc = ''

        while len(s) > 0:
            i = 0

            #第一轮字符
            c = s[0]
            while (i < len(s) and s[i] == c):
                i += 1
            acc += str(i) + c
            if i == len(s):
                break
            else:
                s = s[i:]
        return acc
    for i in range(1, n):
        seq[i] = int(say(str(seq[i-1])))
    return seq

list = look_and_say(31)
item = look_and_say(31)[30]
print item, type(item)
print len(str(item))
