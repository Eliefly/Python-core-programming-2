# -*- coding: utf-8 -*-
# !/usr/bin/python3.5
import os


def readNwriteTextFiles(fname, mode):
    if mode == 'create':
        ls = os.linesep

        # get filename
        while True:
            # fname = input('Please enter a file name: ')
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
    elif mode == 'read':
        try:
            fobj = open(fname, 'r')
        except IOError as e:
            print('file open error:', e)
        else:
            # display contents to the screen
            for eachLine in fobj:
                print(eachLine)
            fobj.close()

# 测试：
# from Q3_12 import readNwriteTextFiles
# readNwriteTextFiles('test.txt', 'create')
# readNwriteTextFiles('test.txt', 'read')