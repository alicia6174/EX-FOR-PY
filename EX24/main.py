#!/usr/bin/python
import sys

def isAnagram(s1, s2):
    if (not len(s1) == len(s2)):
        print "Not of the same length."
        sys.exit()
    for i in range(1, len(s1)):
        if (not s1.count(s1[i]) == s2.count(s2[i])):
            return False
    return True

print "Enter two strings and I'll tell you if they\nare anagrams:"
s1 = raw_input("Enter the first string: ")
s2 = raw_input("Enter the second string: ")
if (isAnagram(s1, s2) == True):
    print "\"%s\" and \"%s\" are anagrams." % (s1, s2)


