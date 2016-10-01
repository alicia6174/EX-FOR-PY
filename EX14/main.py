#!/usr/bin/python
import math

def cntTol():
    sub = float(raw_input("What is the order amount? "))
    ste = raw_input("What is the state? ")
    prt = "The total is $%.2f."% sub
    if (ste == "WI"):
        prt = "The subtotal is $%.2f.\nThe tax is $0.55.\nThe total is $%.2f." \
        % (sub, sub+0.55)
    print prt

cntTol()
