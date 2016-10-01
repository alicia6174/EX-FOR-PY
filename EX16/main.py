#!/usr/bin/python

def cnkAge():
    age = int(raw_input("What is your age? "))
    print "You are old enough to legally drive." if age >= 16\
            else "You are not old enough to legally drive."

cnkAge()
