# 第10章 错误和异常
标签（空格分隔）： python-core-2

---
10-1 引发异常。以下的哪个因素会在程序执行是引发异常？注意这里我们问的**并不是异常的原因**。
a)用户；
b)解释器；
c)程序；
d)以上所有；
e)只有b)和c)；
f)只有a)和c)；
```
解释器和程序。引发也叫触发，抛出或者生成。只要检测到错误并意识到异常条件，解释器会引发一个异常，
通过它通知当前控制流有错误发生。Python 也允许程序员自己引发异常。
```

10-2 引发异常。参考上边问题的列表，哪些因素会在执行交互解释器时引发异常？
```
d
```

10-3 关键自。用来引发异常的关键字有哪些？
```
try-except-finally, assert, raise, with
```
10-4 关键字。try-except 和 try-finally 有什么不同？
```
try-except：只有当try代码模块捕获到异常时，except代码模块执行。
try-finally： 无论try代码模块是否有异常，finally代码模块都将执行。
```

10-5.异常。下面这些交互解释器下的Python代码段分别会引发什么异常(参阅表10.2给出的内建异常清单)：
```
>>> if 3 < 4 then:print '3 is less than 4!'
  File "<stdin>", line 1
    if 3 < 4 then:print '3 is less than 4!'
                ^
SyntaxError: Missing parentheses in call to 'print'
>>> aList = ['Hello','World','Anyone',
... 'Home?']
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> x = 4 % 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> import math
>>> i = math.sqrt(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
```
10–6. 改进的 open(). 
为内建的 open() 函数创建一个封装. 使得成功打开文件后, 返回文件句柄; 若打开失败则返回给调用者 None , 而不是生成一个异常. 这样你打开文件时就不需要额外的异常处理语句
```
# -*- coding: utf-8 -*-

def myopen(file, mode='r', buffering=-1, encoding=None, 
    errors=None, newline=None, closefd=True, opener=None):
    
    try:
        ret = open(file, mode='r', buffering=-1, encoding=None, 
            errors=None, newline=None, closefd=True, opener=None)
    except IOError:
        ret = None

    return None
# 123.txt is not exist 
print(myopen('123.txt'))  # None
```

10-7.异常。下面两端Python伪代码a)和b)有什么区别？考虑语句A和B的上下文环境。(这么细致的区别要感谢Guido!)
```
(a) 
try:
    statement_A
except . . .:
    . . .
else:
    statement_B
(b) 
try:
    statement_A
    statement_B
except . . .:
    . . .
```
```
(a)是监测 statement_A 的异常，如果没有异常才执行  statement_B.
(b)是同时监测 statement_A 和  statement_B 的异常。
```


10–8. 改进的 raw_input() . 
本章的开头, 我们给出了一个"安全"的 float() 函数,它建立在内建函数 float() 上, 可以检测并处理 float() 可能会引发的两种不同异常. 同样,raw_input() 函数也可能会生成两种异常, EOFError (文件末尾 EOF, 在 Unix 下是由于按下了Ctrl+D 在 Dos 下是因为 Ctrl+Z) 或是 KeyboardInterrupt ( 取消输入, 一般是由于按下了Ctrl+C). 请创建一个封装函数 safe_input() , 在发生异常时返回 None
```
# -*- coding: utf-8 -*-

def safe_input(prompt=None):
    try:
        ret = input(prompt)
    except (KeyboardInterrupt, EOFError):
        ret = None

    return ret

a = safe_input('input: ')
print(a)
```

10–9. 改进的 math.sqrt(). 
math 模块包含大量用于处理数值相关运算的函数和常量. 不幸的是, 它不能识别复数, 所以我们创建了 cmath 模块来支持复数相关运算. 请创建一个safe_sqrt() 函数, 它封装 math.sqrt() 并能处理负值, 返回一个对应的复数.
```
# -*- coding: utf-8 -*-
import cmath, math

def safe_sqrt(num):
    try:
        if num >= 0:
            ret = math.sqrt(num)
        else:
            ret = cmath.sqrt(num)
    except TypeError:
        ret = None

    return ret

print(safe_sqrt('1'))
print(safe_sqrt(4))
print(safe_sqrt(-3))
```



