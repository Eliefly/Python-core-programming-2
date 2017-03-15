# -*- coding: utf-8 -*-
# !/usr/bin/python3.5

import os

def readNwriteTextFiles(fname, mode):
    ls = os.linesep

    if mode == 'write':
        # 如果文件已存在，则打开修改文件
        if os.path.exists(fname):
            os.system('vim' + ' ' + fname)  # 调用vim修改文件
        # 如果文件不存在，则新建文件
        else:
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

