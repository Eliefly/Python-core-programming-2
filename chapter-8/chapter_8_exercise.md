# 第8章 条件和循环


---
##### 8-1
```
def test(x):
    print('A')
    if x > 0:
        print('B')
    elif x < 0:
        print('C')
    else:
        print('D')
    print('E')

test(1)
```

##### 8–2. 循环. 
编写一个程序, 让用户输入三个数字: (f)rom, (t)o, 和 (i)ncrement . 以 i为步长, 从 f 计数到 t , 包括 f 和 t . 例如, 如果输入的是 f == 2, t == 26, i == 4 , 程序将输出 2, 6, 10, 14, 18, 22, 26.
```
def myrange(start, stop, step):
    ret = start
    while ret <= stop:
        print(ret)
        ret += step

myrange(2, 26, 4)
```

##### 8–3. range() . 
如果我们需要生成下面的这些列表, 分别需要在 range() 内建函数中提供那些参数?
(a) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
(b) [3, 6, 9, 12, 15, 18]
(c) [-20, 200, 420, 640, 860]
```
print([i for i in range(10)])
print([i for i in range(3, 19, 3)])
print([i for i in range(-20, 900, 220)])
```

##### 8–4. 素数. 
我们在本章已经给出了一些代码来确定一个数字的最大约数或者它是否是一个素数. 请把相关代码转换为一个返回值为布尔值的函数，函数名为 isprime() . 如果输入的是一个
素数, 那么返回 True , 否则返回 False .
```
def isprime(num):
    num = abs(num)
    ret = True
    if num < 2:
        ret = False
    for i in range(2, num):
            if num % i == 0:
                ret = False
    return ret

print([i for i in range(100) if isprime(i)])
```
##### 8–5. 约数. 
完成一个名为 getfactors() 的函数. 它接受一个整数作为参数, 返回它所有约数的列表, 包括 1 和它本身。
```
def getfactors(num):  
    return [i for i in range(1, num+1) if num % i == 0]  
  
print(get_factors(100)) 
```
##### 8–6. 素因子分解. 
以刚才练习中的 isprime() 和 getfactors() 函数为基础编写一个函数, 它接受一个整数作为参数, 返回该整数所有素数因子的列表. 这个过程叫做求素因子分解, 它输出的所有因子之积应该是原来的数字. 注意列表里可能有重复的元素. 例如输入 20 , 返回结果应该是 [2, 2, 5] .
借助`isprime()`和`getfactors()`:
```
def isprime(num):
    num = abs(num)
    ret = True
    if num < 2:
        ret = False
    for i in range(2, num):
            if num % i == 0:
                ret = False
    return ret

def getfactors(num):  
    return [i for i in range(1, num+1) if num % i == 0]  
  
def solvenum(num):
    ret = []
    if num == 1 or num == 0:
        return [num]
    while True:
        if isprime(num):
            ret.append(num)
            break
        else:
            tmp = getfactors(num)
            tmp.remove(1)
            factor = min(tmp)
            ret.append(factor)
            num = num // factor
    return ret

print(solvenum(1))
```
直接实现：
```
def solvenum(num):
    ret = []
    done = True
    while done:
        for i in range(2, num+1):
            if i == num:
                ret.append(num)
                done = False
                break
            if num % i == 0:
                ret.append(i)
                num = num // i
                break

    return ret

print(solvenum(20))
```
##### 8–7. 完全数. 
完全数被定义为这样的数字: 它的约数(不包括它自己)之和为它本身. 例如: 6的约数是 1, 2, 3, 因为 1 + 2 + 3 = 6 , 所以 6 被认为是一个完全数. 编写一个名为 isperfect()的函数, 它接受一个整数作为参数, 如果这个数字是完全数, 返回 1 ; 否则返回 0 .
```
def isperfect(num):  
    factors = [i for i in range(1, num) if num % i == 0]  
    if sum(factors) == num:
        print(factors, num)
        return 1
    else:
        return 0

[i for i in range(1, 10000) if isperfect(i)]

# [1, 2, 3] 6
# [1, 2, 4, 7, 14] 28
# [1, 2, 4, 8, 16, 31, 62, 124, 248] 496
# [1, 2, 4, 8, 16, 32, 64, 127, 254, 508, 1016, 2032, 4064] 8128
```
##### 8–8. 阶乘. 
一个数的阶乘被定义为从 1 到该数字所有数字的乘积. N 的阶乘简写为 N! .写一个函数, 指定N, 返回 N! 的值.
```
def factorial(num):
    ret = 1
    for i in range(1, num+1):
        ret *= i

    return ret

print(factorial(10))    # 3628800
```
```
from functools import reduce

def factorial(num):
    multiply = lambda x, y: x * y
    return  reduce(multiply, range(1, num+1))

print(factorial(10))
```
##### 8–9. Fibonacci 数列. 
Fibonacci 数列形如 1, 1, 2, 3, 5, 8, 13, 21, 等等. 也就是说,下一个值是序列中前两个值之和. 写一个函数, 给定 N , 返回第 N 个 Fibonacci 数字. 例如, 第1 个 Fibonacci 数字是 1 , 第 6 个是 8 .
```
from math import ceil
def fibonacci(nrd):
    if nrd == 1 or nrd == 2:
        return 1
    a = b = 1
    n = ceil(nrd/2 - 1) # ceil 进1计算
    for i in range(n):
        a, b = a+b, a+2*b
    return b if nrd%2 == 0 else a

print([fibonacci(i) for i in range(1, 20)])
```
##### 8–10. 文本处理. 
统计一句话中的元音, 辅音以及单词(以空格分割)的个数. 忽略元音和辅音的特殊情况, 如 "h", "y", "qu" 等. 附加题: 编写处理这些特殊情况的代码.
```
def countvowel(a_str):
    vowel = 'aeiouAEIOU'
    sum_vowel = 0
    sum_consonant = 0
    for ch in a_str:
        if ch.isalpha():  # 是否是字母
            if ch in vowel:
                sum_vowel += 1
            else:
                sum_consonant += 1

    word_lst = a_str.split(' ')
    sum_word = 0
    for word in word_lst:
        if word[0].isalpha() is True:   # 首字符是字母的就是单词
            sum_word += 1

    return (sum_vowel, sum_consonant, sum_word)

# 数字不认为是单词
a_str = '123 We Are looking for a great Senior Python Developer!'
print(countvowel(a_str))    # (18, 24, 9)

a_str = 'a, e i o u!'
print(countvowel(a_str))    # (5, 0, 5)
```
8–11. 文本处理.
要求输入一个姓名列表，输入格式是“Last Name, First Name,” 即 姓,逗号, 名. 编写程序处理输入, 如果用户输入错误, 比如“First Name Last Name,” , 请纠正这些错误, 并通知用户. 同时你还需要记录输入错误次数. 当用户输入结束后, 给列表排序, 然后以“姓 , 名" 的顺序显示.
输入输出示例(你不需要完全按照这里里例子完成):
```
% nametrack.py
Enter total number of names: 5
Please enter name 0: Smith, Joe
Please enter name 1: Mary Wong
>> Wrong format... should be Last, First.
>> You have done this 1 time(s) already. Fixing input... 
Please enter name 2: Hamilton,Gerald
Please enter name 3: Royce, Linda
Please enter name 4: Winston Salem
>> Wrong format... should be Last, First.
>> You have done this 2 time(s) already. Fixing input...
The sorted list (by last name) is:
Hamilton, Gerald
Royce, Linda
Salem, Winston
Smith, Joe
Wong, Mary
```
其他的异常输入不考虑：
```
def nametrack():
    num_name = int(input('Enter total number of names: '))
    fix_index = 1
    name_lst = []
    for index in range(num_name):
        str_name = input('Please enter name %s: ' % index)
        if ',' not in str_name:
            print('Wrong format... should be Last, First.')
            print('You have done this %s time(s) already. Fixing input...' % fix_index)
            fix_index += 1
            tmp = str_name.split()
            str_name = ', '.join(tmp[-1::-1])
            print(str_name)
        name_lst.append(str_name)
    name_lst.sort()
    print('The sorted list (by last name) is: ')
    for name in name_lst:
        print(name)

if __name__ == '__main__':
    nametrack()
```

##### 8–12. (整数)位操作.

编写一个程序, 用户给出起始和结束数字后给出一个下面这样的表格,分别显示出两个数字间所有整数的十进制, 二进制, 八进制和十六进制表示. 如果字符是可打印的ASCII 字符, 也要把它打印出来, 如果没有一个是可打印字符, 就省略掉 ASCII 那一栏的表头.
```
from string import printable

def display(start, stop):
    print('   输入的起始值： %s' % start)
    print('   输入的结束值： %s' % stop)
    title = 'DEC      BIN    OCT   HEX  '
    for num in range(start, stop+1):
        if chr(num) in printable:
            title = title + 'ASCII'
            break
    print(title)
    print('-'*35)
    for num in range(start, stop+1):
        print('%-6s%06s%6o%6x    ' % (num, bin(num)[2:], num, num), end='')
        if chr(num) in printable:
            print(chr(num))
        else:
            print()


display(14, 18)
display(26, 41)
```

##### 8-13 程序执行性能。
在8.5.2节里，我们介绍了两种基本迭代序列方法：（1）通过序列项，（2）通过序列索引遍历。该小节的末尾我们指出后一种方法在序列很长的时候性能不佳，你认为他的原因是什么？
```
# 可能是通过序列索引遍历，访问元素时还需要用索引去访问元素值。

import time
def compare():
    strtime=time.time()
    alist=range(1000000)
    for i in range(len(alist)):   # 运行时间：  1.809143
        print(alist[i])
    # for i in alist:             # 运行时间：  1.6526049999999999
    #    print(i)
    endtime=time.time()   
    print("运行时间： ", (endtime-strtime))
compare()
```

