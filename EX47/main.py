#!/usr/bin/python
import json
import urllib

url = 'http://api.open-notify.org/astros.json'
#url = 'http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false'
output = json.load(urllib.urlopen(url))

# This data is a string.
# Use json.dumps() to avoid "abc" from changing to unicode u'abc'
data = json.dumps(output)

# This data is a dictionary.
data = eval(data)
print data

number = data.values()[1]
print "There are %d people in space right now:" % \
         number
for i in range(0, number):
    print "%s: %s\n"  % \
            (data.values()[2][i]["name"],\
            data.values()[2][i]["craft"])

# This website is easy to result in time-out.
# So I just ouput all the information without put it
# in an evenly-spaced table.
