#!/usr/bin/python

fi = open('input', 'r')
fr = fi.read()

key = 'utilize'
p_old = 0
p_new = fr.find(key)
cnt = 0 # count the number of key

fo = open('output', 'w+')
cur = 0
while cur != len(fr)-1:
    if cur == (p_old+p_new+cnt):
        fo.write('use')
        cur += 7
        # search the next position of key
        cnt += 1
        p_old = p_new
        p_new = fr[p_old+cnt:len(fr)].find(key)
    else:
        fo.write(fr[cur])
        cur += 1

fo.close()
fi.close()
