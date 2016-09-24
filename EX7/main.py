#!/usr/bin/python

def cntArea():
    x = int(raw_input("What is the length of the room in feet? "))
    y = int(raw_input("What is the width of the room in feet? "))
    c = 0.09290304
    f2 = x*y
    m2 = f2*c
    print "You entered dimensions of %d feet by %d feet.\nThe area is\n%d square feet\n%.3f square meters" % \
            (x, y, f2, m2)

cntArea()
