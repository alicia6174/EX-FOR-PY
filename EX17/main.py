#!/usr/bin/python

def cnkBAC():
    W = float(raw_input("Your weight: "))
    g = int((raw_input("Your gender (1 for men / 2 for women): ")))
    A = float(raw_input("Total alcohol consumed: "))
    H = float(raw_input("Time since your last drink: "))
    r = 0.73 if g == 1 else 0.66
    BAC = (A * 5.14) / (W * r) - 0.015 * H
    print "Your BAC is %.2f\nIt is not legal for you to drive." %BAC\
            if BAC >= 0.08 else "OK"

cnkBAC()
