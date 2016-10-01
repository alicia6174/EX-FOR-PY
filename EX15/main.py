#!/usr/bin/python

def chkPass():
    pas = "abc$123"
    key = raw_input("What is the password? ")
    if (key == pas):
        print "Welcome!"
    else:
        print "I don't know you."

chkPass()
