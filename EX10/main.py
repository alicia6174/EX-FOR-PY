#!/usr/bin/python

import operator

def inputItem(i):
    x = int(raw_input("Enter the price of item %d: " % i))
    y = int(raw_input("Enter the quantity of item %d: " % i))
    return x*y

def showPrice(a):
    print("{0:s}: ${1:.2f}").format(a[0], a[1])

def selfCheck():
    Sub = reduce(operator.add, map(inputItem, range(1,4)))
    Tax = Sub*0.055
    Prt = [('Subtotal', Sub), ('Tax', Tax), ('Total', Sub+Tax)]
    map(lambda arr : showPrice(arr), Prt)

selfCheck()
