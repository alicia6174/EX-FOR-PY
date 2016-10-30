#!/usr/bin/python

# read file
f = open('words.txt', 'r')
fr = f.read()

wds = {}
tmp = []

cur_tmp = 0
for i in range(0, len(fr)):
    if (fr[i].isalpha()):
        tmp.insert(cur_tmp, fr[i])
        cur_tmp += 1
    elif (fr[i] == " " or fr[i] == '\n'):
        if ("".join(tmp)+':' in wds.keys()):
            wds["".join(tmp)+':'] += 1
        elif ~("".join(tmp)+':' in wds.keys()):
            wds["".join(tmp)+':'] = 1
        tmp = []

# dictionary to list
keys =  wds.keys()
values = wds.values()
wds_list = []
for j in range(0, len(keys)):
    wds_list.insert(j, [keys[j], values[j]]);

# sort & count stars
wds_list = sorted(wds_list, reverse = False)
for k in range(0, len(keys)):
    star_tmp = []
    cur_star_tmp = 0
    for m in range(0, wds_list[k][1]):
        star_tmp.insert(cur_star_tmp, '*')
        cur_star_tmp += 1
    wds_list[k].insert(2, "".join(star_tmp))

# ouput an evenly spaced table (ref.#42)
class MyClass(object):
    def __init__(self, a, b):
        self.keys = a
        self.stars = b

headers = ['keys', 'stars']
items = []
for i in range(0,len(wds_list)):
    items.insert(i, MyClass(wds_list[i][0], wds_list[i][2]))
items = tuple(items)
item_lens = [[getattr(item, x) for x in headers] for item in items]
max_lens = [len(str(max(i, key=lambda x: len(str(x))))) for i in zip(*[headers] + item_lens)]
for i in items:
    print ' '.join('{0:{width}}'.format(x, width=y) for x, y in zip([getattr(i, x) for x in headers], max_lens))

