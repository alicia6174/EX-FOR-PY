#!/usr/bin/python
import random

x = raw_input("Enter a name: ")
A = ['0']
i = 1
while (x != ""):
    A.insert(i, x)
    i += 1
    x = raw_input("Enter a name: ")
n = random.randint(1,len(A)-1)
print "The winner is... %s." % A[n]


