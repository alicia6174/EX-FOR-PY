#!/usr/bin/python

import time

def calRet():
    x = raw_input("What is your current age? ")
    y = raw_input("At what age would you like to retire? ")
    z = time.strftime("%Y")
    print "You have %d years left until you can retire.\nIt's %d, so you can retire in %d." % \
            (int(y)-int(x), int(z), int(z)+int(y)-int(x))

calRet()
