#!/usr/bin/python

def cntPizza():
    x = int(raw_input("How many people? "))
    y = int(raw_input("How many pizzas do you have? "))
    z = int(raw_input("What is the number of slices per pizza? "))
    q = y*z/x
    r = y*z-x*q
    print "%d people with %d pizzas\nEach person gets %d pieces of pizza.\nThere are %d leftover pieces." % \
            (x, y, q, r)

cntPizza()
