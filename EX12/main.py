#!/usr/bin/python
import math

def cntInterest():
    P = int(raw_input("Enter the principal: "))
    r = float(raw_input("Enter the rate of interest: "))
    t = int(raw_input("Enter the number of years: "))
    A = int(round(P*(1+r*t/100)))
    print "After %d years at %.1f" % (t,r) + "%" + ", the investment will\nbe worth $%d." % A

cntInterest()
