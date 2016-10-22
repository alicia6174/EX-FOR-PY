#!/usr/bin/python

f = open('data', 'r')
Data = f.readlines()
fs = lambda string: string[0:len(string)-1].split(',')
Data = map(fs, Data)

class MyClass(object):
    def __init__(self, a, b, c):
        self.Last = a
        self.First = b
        self.Salary = c

headers = ['Last', 'First', 'Salary']
items = []
for i in range(0,len(Data)):
    items.insert(i, MyClass(Data[i][0], Data[i][1], Data[i][2]))
items = tuple(items)
item_lens = [[getattr(item, x) for x in headers] for item in items]
max_lens = [len(str(max(i, key=lambda x: len(str(x))))) for i in zip(*[headers] + item_lens)]
H = ' '.join('{0:{width}}'.format(x, width=y) for x, y in zip(headers, max_lens))
print H
print "".join(['-']*len(H))
for i in items:
    print ' '.join('{0:{width}}'.format(x, width=y) for x, y in zip([getattr(i, x) for x in headers], max_lens))


