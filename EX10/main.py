#!/usr/bin/python

def inputItem(i):
    x = int(raw_input("Enter the price of item %d: " % i))
    y = int(raw_input("Enter the quantity of item %d: " % i))
    return x*y

def showPrice(a, b):
    print "%s: $%.2f" % (a, b)

def selfCheck():
    Idx = [1, 2, 3]
    Itm = map(inputItem, Idx)
    Add = lambda x,y : x+y
    Sub = reduce(Add, Itm)
    Tax = Sub*0.055
    Prt = [('Subtotal', Sub), ('Tax', Tax), ('Total', Sub+Tax)]
    map(lambda arr : showPrice(arr[0], arr[1]), Prt)

selfCheck()
