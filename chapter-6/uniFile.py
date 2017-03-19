#-*- coding: UTF-8 -*-
# !/usr/bin/python2.7

'''
读写Unicode strings 的实例：用 utf-8 编码写人Unicode string 一文件，然后读取。

注意：程序是在 Python2.7 下运行的。
''' 

CODEC = 'utf-8'
FILE = 'unicode.txt'

hello_out = u"hello world\n"
bytes_out = hello_out.encode(CODEC)
f = open(FILE, 'w')
f.write(bytes_out)
f.close()

f = open(FILE, 'r')
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)
print(hello_in)