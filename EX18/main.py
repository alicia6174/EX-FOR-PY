#!/usr/bin/python
import math
import sys

def cvtTem():
    print "Press C to convert from Fahrenheit to Celsius."
    print "Press F to convert from Celsius to Fahrenheit."
    x = raw_input("Your choice: ")
    if not x in ['c', 'C', 'f', 'F']:
        print "Please input C or F."
        sys.exit()
    print " "

    s = "Please enter the temperature in "
    t = int(raw_input(s + "Celsius: ")) if (x == 'f') or (x == 'F')\
        else int(raw_input(s + "Fahrenheit: "))

    s = "The temperature in "
    print s + "%s is %d." % ('Fahrenheit', (t*9/5)+32)\
        if (x == 'f') or (x == 'F')\
        else s + "%s is %d." % ('Celsius', (t-32)*5/9)

cvtTem()
