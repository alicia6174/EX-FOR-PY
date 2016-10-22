#!/usr/bin/python

f = open('data', 'r')
Data = f.readlines()
Data.sort()
print "Total of %d names" % len(Data)
print "-----------------"
for i in range(0, 7):
    s = Data[i]
    print s[0:len(s)-1]
# Why does the answer put "Ling, Mai" in the 1st place
# while it asks us to print the data  alphabetically?

