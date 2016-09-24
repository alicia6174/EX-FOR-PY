#!/usr/bin/python

import math

def cntGallon():
    x = int(raw_input("What is the length? "))
    y = int(raw_input("What is the width? "))
    a = x*y
    c = 350
    q = math.ceil(a/350.0)
    print "You will need to purchase %d gallons of" % q
    print "paint to cover %d square feet." % a

cntGallon()
