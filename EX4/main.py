#!/usr/bin/python

def madLib():
    x = raw_input("Enter a noun: ")
    y = raw_input("Enter a verb: ")
    z = raw_input("Enter an adjective: ")
    w = raw_input("Enter an adverb: ")
    s = "Do you verb your adjective noun adverb? That's hilarious!"
    print s.replace('noun', x).replace('verb', y, 1) \
            .replace('adjective', z).replace('adverb', w)

madLib()
