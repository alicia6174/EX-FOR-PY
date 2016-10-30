#!/usr/bin/python
import os
import sys

site_name = raw_input("Site name: ")
author = raw_input("Author: ")
java = raw_input("Do you want a folder for JavaScript? ")
css = raw_input("Do you want a folder for CSS? ")

#path = "/Users/guan/Desktop/EX-FOR-PY/EX43/awesomeco"
path = "/Users/guan/Desktop/EX-FOR-PY/EX43/"+site_name
if not os.path.exists(path):
    os.makedirs(path, 0755);
print "Created ./"+site_name

newfile = os.path.join(path, 'index.html')
f = open(newfile, 'w')
cont = \
"\
<html>\n \
<head>\n \
<title>"+site_name+"</title>\n \
<meta name=\"author\" content=\""+author+"\"/>\n \
</head>\n \
</html> \
"
f.write(cont)
print "Created ./"+site_name+"/index.html"

if java == 'y':
    path = "/Users/guan/Desktop/EX-FOR-PY/EX43//awesomeco/js"
    if not os.path.exists(path):
        os.makedirs(path, 0755);
    print "Created ./awesomeco/js/"

if css == 'y':
    path = "/Users/guan/Desktop/EX-FOR-PY/EX43//awesomeco/css"
    if not os.path.exists(path):
        os.makedirs(path, 0755);
    print "Created ./awesomeco/css/"

