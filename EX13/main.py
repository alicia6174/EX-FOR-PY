#!/usr/bin/python
import math

def cntInterest():
    P = int(raw_input("What is the principal amount? "))
    r = float(raw_input("What is the rate? "))
    t = int(raw_input("What is the number of years? "))
    n = int(raw_input("What is the number of times the interest is compounded per year? "))
    A = P * pow(1+r/100/n, n*t)
    print "$%d invested at %.1f" % (P, r) + "%" + " for %d years\ncompounded %d times per year is $%.2f." \
    % (t, n, A)

cntInterest()
