import os, re
import sys
import fileinput

tempfile = open("서울특별시.utf8.txt", 'r')
lines = tempfile.read()
# while True:
new_lines = [ i for i in lines.split('|') if re.match(r'^\n\d{5}$', i) ]
# for i in new_lines:
#     if not re.match(r'^\d{5}$', i):
#         new_lines.remove(i)
# for i in new_lines:
    # if re.match(r'^\d{5}$', zip_code):
#         new_lines
# print(new_lines)
tempfile.close()
new_lines[0] = new_lines[0][1:]
f = open("new_서울특별시.txt", 'w')
for x in new_lines:
    f.write(x)
f.close()