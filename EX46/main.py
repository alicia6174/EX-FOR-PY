#!/usr/bin/python

f = open('words.txt', 'r')
fr = f.read()
#print fr
wds = {}
tmp = []
# cur_wds = 0
cur_tmp = 0
for i in range(0, len(fr)):
    if (fr[i].isalpha()):
        tmp.insert(cur_tmp, fr[i])
        cur_tmp += 1
    elif (fr[i] == " " or fr[i] == '\n'):
        if ("".join(tmp) in wds.keys()):
            wds["".join(tmp)] += 1
        elif ~("".join(tmp) in wds.keys()):
            wds["".join(tmp)] = 1
        tmp = []
#print wds
# val = wds.values()
# val = sorted(val, reverse = True)
# print val
# print len(wds)
# for i in range(1, len(val)):
#     for j in range(1, len(val)):
#         if (wds[])
# unfinished...


