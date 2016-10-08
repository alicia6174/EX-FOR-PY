#!/usr/bin/python
import math

def cntTax():
    amt = float(raw_input("What is the order amount? "))
    ste = raw_input("What state do you live in? ")
    tmp = round(amt*100)/100
    tol = tmp
    prt = "The total is $%.2f." % tol

    if (ste == "Wisconsin"):
        cty = raw_input("What county do you live in? ")
        if (cty == "Eau Claire"):
            tax = tmp * 0.05
            tol = tmp * 1.05
        elif (cty == "Dunn"):
            tax = tmp * 0.04
            tol = tmp * 1.04
        prt = "The tax is $%.2f.\nThe total is $%.2f." %(round(tax*100)/100, tol)
    elif (ste == "Illinois"):
        tol = tmp * 1.08
        prt = "The tax is $%.2f.\nThe total is $%.2f." %(round(tax*100)/100, tol)

    print prt

cntTax()

