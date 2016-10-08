#!/usr/bin/python
import math
import sys

def cntBMI():
    w = raw_input("Input your weight in pounds: ")
    if (w.isdigit() == False):
        print "Please input numbers."
        sys.exit()
    h = raw_input("Input your height in inches: ")
    if (h.isdigit() == False):
        print "Please input numbers."
        sys.exit()
    b = float(w)*703/float(h)/float(h)
    print "Your BMI is %.1f." %b
    if (b >= 18.5 and b <= 25):
        print "You are within the ideal weight range."
    elif (b < 18.5):
        print "You are underweight. You should see your doctor."
    else:
        print "You are overweight. You should see your doctor."

cntBMI()

