# -*- coding: utf-8 -*-
# !/usr/bin/python3.5

'readTextFile.py -- read and display text file'

fname = input('Enter filename:')
print('Attempt to open file for reading...')

try:
    fobj = open(fname, 'r')
except IOError as e:
    print('file open error:', e)
else:
    # display contents to the screen
    for eachLine in fobj:
        print(eachLine)
    fobj.close()
