# 第3章 Python基础

---
另可参考：http://blog.csdn.net/reimuko/article/details/28097677
```
# -*- coding: utf-8 -*-
# !/usr/bin/python3.5
```

##### 3-1 为什么python不需要变量名和变量类型声明?
```
在Python中，对象的类型和内存占用都是运行时确定的。在创建变量（即变量被赋值时）时，
解释器会根据语法和右侧的操作数来决定新对象的类型。在对象创建后，一个该对象的引用
会被赋值给左侧的变量。
```
##### 3-2 为什么Python中不需要声明函数类型？
```
和不用声明变量一样，Python不用去声明函数的返回类型，是由于其“若类型”的语言特性决定的。
在其他语言中，例如C/C++语言中在存储一个数据之前，都需要在内存中给这个数据开辟一个固定
的内存空间，并给这个类型空间指定一个唯一的 id（变量名），然后才把要存储的数据放到这个
变量名对于的内存空间中。而Python的做法，是`以数据为中心`，上来就把要存储的数据放到内存，
然后再去用一个变量名`引用`这个数据。
```

##### 3-3 Python中为什么应当避免在变量名的开始和结尾使用双下划线？
```
Pyhton 用下划线作为变量前缀和后缀指定特殊的变量。往往会有特殊的含义。
参见：[关于python中带下划线的变量和函数的意义](http://www.cnblogs.com/elie/p/5902995.html)
```
##### 3-4 Python 一行书写多个语句方式?
```
可以，使用';'可以将多个语句写在同一行。但这样回大大降低代码的可读性，一般不提倡这么做。
```

##### 3-5 Python 同一语句多行书写方式?
```
可以，使用续行符'\'继续上一行，这样一行过长的语句可以分解成几行。
两种例外情况不使用'\'也可以多行书写。
例:(1)在含中括号，小括号，花括号可以多行书写。
给变量赋值时:
a, b, c, d = (1,
2, 3, 4)
(2)三引号的字符串也可跨行书写，书写文档字符串时经常遇到。
'''aaaaaa
111111111'''
```

##### 3-6
```
>>> x, y, z = 1, 2, 3
>>> print(x, y, z)
1 2 3

>>> z, x, y = y, z, x
>>> print(x, y, z)
3 1 2
Python支持“多元”赋值，可以实现无需中间变量交换两个变量的值。
```

##### 3-7
```
不合法：
40XL			数字开头
$saving$		非法字符$ 
0x40L			数字开头
big-daddy		非法字符-
2hot2touch		数字开头
thisIsn'tAVar	非法字符'
True			关键字
if  			关键字
counter-1 		非法字符-

判断是否是Python关键字可用 keyword 模块，如：
>>> import keyword
>>> keyword.iskeyword('if')
True
>>> keyword.iskeyword('print')
False
```

##### 3–12. 合并源文件。
将两段程序合并成一个，给它起一个你喜欢的名字，比方readNwriteTextFiles.py。让用户自己选择是创建还是显示一个文本文件。
```
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
```
##### 3–13. 添加新功能。 
将你上一个问题改造好的 readNwriteTextFiles.py 增加一个新功能：允许用户编辑一个已经存在的文本文件。 你可以使用任何方式，无论是一次编辑一行，还是一次编辑所有文本。需要提醒一下的是， 一次编辑全部文本有一定难度， 你可能需要借助 GUI工具包或一个基于屏幕文本编辑的模块比如 curses 模块。要允许用户保存他的修改（保存到文件）或取消他的修改（不改变原始文件），并且要确保原始文件的安全性（不论程序是否正常关闭）。
```
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
```


