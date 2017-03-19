#-*- coding: UTF-8 -*-
# !/usr/bin/python3.5 

'''
读写Unicode strings 的实例：用 utf-8 编码写人Unicode string 一文件，然后读取。

注意：程序是在 Python3.5 下运行的。
''' 

CODEC = 'utf-8'
FILE = 'unicode.txt'

hello_out = u"hello world\n"
print(type(hello_out))	# <class 'str'>

# bytes_out = hello_out.encode(CODEC)
f = open(FILE, 'w')
# f.write(bytes_out)	# python3.5： write() argument must be str, not bytes		
f.write(hello_out)
f.close()

f = open(FILE, 'r')
bytes_in = f.read()
f.close()
# hello_in = bytes_in.decode(CODEC)
# print(hello_in)
print(bytes_in)