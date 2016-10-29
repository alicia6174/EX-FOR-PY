#!/usr/bin/python
import json
import sys

with open("data.txt") as f:
    data = json.load(f)

while 1:
    keyin = raw_input("What is the product name? ")
    for i in range(0, 3):
        if (data["products"][i]["name"] == keyin):
            print "Name: %s\nPrice: $%.2f\nQuantity on hand: %d" % \
                (keyin, float(data["products"][i]["price"]), int(data["products"][i]["quantity"]))
            sys.exit()
    print "Sorry, that product was not found in our inventory."

