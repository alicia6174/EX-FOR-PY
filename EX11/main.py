#!/usr/bin/python
import math

def cntUSD():
    amt_from = int(raw_input("How many euros are you exchanging? "))
    rat_from = float(raw_input("What is the exchange rate? "))
    amt_to = round(amt_from * rat_from) / 100
    print "%d euros at an exchange rate of %.2f is\n%.2f U.S. dollars." % \
    (amt_from, rat_from, amt_to)

cntUSD()
