#-*- coding: UTF-8 -*-
# !/usr/bin/python3.5

import sys
import locale
 
def p(f):
    print('%s.%s(): %s' % (f.__module__, f.__name__, f()))
 
# 返回当前系统所使用的默认字符编码
p(sys.getdefaultencoding)
 
# 返回用于转换Unicode文件名至系统文件名所使用的编码
p(sys.getfilesystemencoding)
 
# 获取默认的区域设置并返回元祖(语言, 编码)
p(locale.getdefaultlocale)
 
# 返回用户设定的文本数据编码
# 文档提到this function only returns a guess
p(locale.getpreferredencoding)
 

# 在笔者的Ubuntu上：
# sys.getdefaultencoding(): ascii
# sys.getfilesystemencoding(): UTF-8
# locale.getdefaultlocale(): ('en_US', 'UTF-8')
# locale.getpreferredencoding(): UTF-8