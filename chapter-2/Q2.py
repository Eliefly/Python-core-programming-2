# -*- coding: utf-8 -*-
# !/usr/bin/python3.5

# 2-5
n = 0
while n <= 10:
    print(n, end=' ')
    n += 1

for n in range(11):
    print(n)

# 2-6
number = input('Please input a number:')
n = int(number)

if n == 0:
    print('this number is 0')
elif n > 0:
    print('this number is postive')
elif n < 0:
    print('this number is negative')

# 2-7
str = '1234'
n = 0
while n < len(str):
    print(str[n])
    n += 1

str = '1234'
for ch in str:
  print(ch)

# 2-8
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

# 2-9
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

# 2-11

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

# 2-12
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

# 2-13
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

# 2-15
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
