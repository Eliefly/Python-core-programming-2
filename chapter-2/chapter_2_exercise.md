# 第2章 数据类型

---
另可参考：http://blog.csdn.net/reimuko/article/details/28093687
```
# -*- coding: utf-8 -*-
# !/usr/bin/python3.5
```
##### 2-1
略

##### 2-2
略

##### 2-3
略

##### 2-4
略

##### 2–5. 循环和数字
分别使用while 和for 创建一个循环:
(a) 写一个while 循环，输出整数从0 到10。（要确保是从0 到10， 而不是从0 到9 或从1 到10）
(b) 做同 (a) 一样的事， 不过这次使用 range() 内建函数。
```
n = 0
while n <= 10:
    print(n, end=' ')
    n += 1

for n in range(11):
    print(n)
```
##### 2–6. 条件判断 
判断一个数是正数，还是负数， 或者等于 0. 开始先用固定的数值，然后修改你的代码支持用户输入数值再进行判断。
```
number = input('Please input a number:')
n = int(number)

if n == 0:
    print('this number is 0')
elif n > 0:
    print('this number is postive')
elif n < 0:
    print('this number is negative')
```
##### 2–7.循环和字串 
从用户那里接受一个字符串输入，然后逐字符显示该字符串。先用while 循环实现，然后再用 for 循环实现。
```
str = '1234'
n = 0
while n < len(str):
    print(str[n])
    n += 1

str = '1234'
for ch in str:
  print(ch)
```
##### 2–8. 循环和运算符 
创建一个包含五个固定数值的列表或元组，输出他们的和。然后修改你的代码为接受用户输入数值。 分别使用while 和for 循环实现。
```
lst = [1, 2, 3, 4, 5]
sum = 0
i = 0
while i < len(lst):
    sum += lst[i]
    i += 1
print(sum)

lst = [1, 2, 3, 4, 5]
sum = 0
for i in lst:
    sum += i
print(sum)
```
##### 2–9.循环和运算符 
创建一个包含五个固定数值的列表或元组，输出他们的平均值。本练习的难点之一是通过除法得到平均值。 你会发现整数除会截去小数，因此你必须使用浮点除以得到更精确的结果。 float()内建函数可以帮助你实现这一功能。
```
lst = [1, 2, 3, 4, 5, 1]
sum = 0
for i in lst:
    sum += i

avg = float(sum/len(lst))
print(avg)

# 2-10
while True:
    n = input('Please input a number between 1 to 100:')
    n = int(n)
    if n >=1 and n <= 100:
        break
    else:
        print('Entered number error!')
```
##### 2–10.带循环和条件判断的用户输入 
使用raw_input()函数来提示用户输入一个1 和100 之间的数，如果用户输入的数满足这个条件，显示成功并退出。否则显示一个错误信息然后再次提示用户输入数值，直到满足条件为止。
略

##### 2–11.带文本菜单的程序 
写一个带文本菜单的程序，菜单项如下（1）取五个数的和 (2) 取五个数的平均值....（X）退出。由用户做一个选择，然后执行相应的功能。当用户选择退出时程序结束。这个程序的有用之处在于用户在功能之间切换不需要一遍一遍的重新启动你的脚本。（这对开发人员测试自己的程序也会大有用处）
```
def fun(option, *args):
    sum = 0
    for i in range(5):
        sum += args[i]
    if 0 == option:
        return sum
    elif 1 == option:
        return sum/5
option = 0
sum = fun(option, 1, 2, 3, 4, 5)
print('Sum of five number: %s' % sum)
option = 1
avg = fun(option, 1, 2, 3, 4, 5)
print('Average of five number: %s' % avg)
```
###### 2-12
```
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__',
 'a', 'n']

>>> dir
<built-in function dir>

>>> type(dir)
<class 'builtin_function_or_method'>

>>> print(dir.__doc__)
dir([object]) -> list of strings

If called without an argument, return the names in the current scope.
Else, return an alphabetized list of names comprising (some of) the attributes
of the given object, and of attributes reachable from it.
If the object supplies a method named __dir__, it will be used; otherwise
the default dir() logic is used and returns:
  for a module object: the module's attributes.
  for a class object:  its attributes, and recursively the attributes
    of its bases.
  for any other object: its attributes, its class's attributes, and
    recursively the attributes of its class's base classes.
```
###### 2-13
```
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

>>> import sys
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__',
 'sys']
>>>
>>> sys.version
'3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)]'

>>> sys.platform
'win32'
```
##### 2–15. 元素排序
(a)让用户输入三个数值并将分别将它们保存到3个不同的变量中。不使用列表或排序算法，自己写代码来对这三个数由小到大排序。
(b)修改(a)的解决方案,使之从大到小排序

```
def sort_number(*args):
    lst = list(args)
    for i in range(0, len(lst)-1):
        for j in range(1+i, len(lst)):
            if lst[i] > lst[j]:
                (lst[i], lst[j]) = (lst[j], lst[i])		#python支持多元赋值
                # tmp = lst[i]
                # lst[i] = lst[j]
                # lst[j] = tmp
    return lst

a = input('Please a number:')
b = input('Please a number:')
c = input('Please a number:')

result = sort_number(a, b, c)
print(result)
```




