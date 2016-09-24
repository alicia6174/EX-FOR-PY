#!/usr/bin/python

def cntChar():
    x = raw_input("What is the input string? ")
    n = len(x)
    if (n is 0):
        print "Please enter somthing."
    else:
        print x + " has " + str(n) + " characters."

cntChar()
