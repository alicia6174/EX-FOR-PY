#!/usr/bin/python
import math

x = raw_input("What is the rate of return? ")
while ((x.isdigit() != True) or (int(x) == 0)):
    print "Sorry. That's not a valid input."
    x = raw_input("What is the rate of return? ")
print "It will take %d years to double your initial investment." % \
        math.ceil(72/float(x))



