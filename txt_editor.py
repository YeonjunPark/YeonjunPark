import os, re
import sys
import fileinput

tempfile = open("서울특별시.utf8.txt", 'r')
lines = tempfile.read()
new_lines = [ i for i in lines.split('|') if re.match(r'^\n\d{5}$', i) ]
tempfile.close()
new_lines[0] = new_lines[0][1:]
f = open("new_서울특별시.txt", 'w')
for x in new_lines:
    f.write(x)
f.close()