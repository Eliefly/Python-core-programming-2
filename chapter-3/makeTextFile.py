# -*- coding: utf-8 -*-
# !/usr/bin/python3.5

'makeTextFIle.py -- create text file'

import os
ls = os.linesep

# get filename
while True:
    fname = input('Please enter a file name: ')
    if os.path.exists(fname):
        print('ERROR: %s already exists' % fname)
    else:
        break

# get file content lines
all = []
print("\nEnter lines ('.' by itself to quit).\n")

# loop until user terminates input
while True:
    entry = input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print('DONE!')
