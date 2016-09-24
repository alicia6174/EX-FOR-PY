#!/usr/bin/python

import operator

## Guan
def doMath():
    x = int(raw_input("What is the first number? "))
    y = int(raw_input("What is the second number? "))
    print "%d + %d = %d\n%d - %d = %d\n%d * %d = %d\n%d / %d = %d" % \
            (x, y, x+y, x, y, x-y, x, y, x*y, x, y, x/y)

#doMath()

## Hsin
x = int(raw_input("What is the first number? "))
y = int(raw_input("What is the second number? "))

op = [('+', lambda x,y : x+y),\
      ('-', lambda x,y : x-y),\
      ('*', lambda x,y : x*y),\
      ('/', lambda x,y : x/y)]

# Method.1
def doMath(o, f, x, y):
    print "%d %s %d = %d" % (x, o, y, f(x,y))

F = lambda arr : doMath(arr[0], arr[1], x, y)
map(F, op)

# Method.2
for arr in op:
    print "%d %s %d = %d" % (x, arr[0], y, arr[1](x,y))

