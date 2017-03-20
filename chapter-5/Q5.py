#-*- coding: UTF-8 -*-
# !/usr/bin/python3.5

# 5-1 整型。讲讲Python普通整型和长整型的区别。
普通整型：
Python 中普通整型等价于C的（有符号）长整型。
在32位机器上，取值范围是 -2^31 ~ 2^31 - 1 ，也就是 -2 147 483 647 ~ 2 147 483 647；
在64位机器上使用64位编译器编译python，那么这个系统的整型将是64位；
长整型：
Python长整形类型能表达的数值仅仅与机器支持的（虚拟）内存大小有关，可以轻松表达很大的整形。这点和C或其它编译型语言的长整形类型有很大的不同。

# 5-2
def multipy(x, y):
    return x * y

print(multipy(3, 6))

# 5-3
def mark(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'    
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif score < 60:
        return 'F'

score = 68
print(mark(score))


# 5-4
def isLeapyear(year):
    if (year%4 == 0 and year%100 != 0) or (year%400 ==0):
        return True
    else:
        return False

print(isLeapyear(2000))
print(isLeapyear(1900))

# 5-5

def changeCoin(dollar):
    if dollar < 0 or dollar >1:
        return ('Please input less 1 dollar.')
    coins = 100 * dollar
    c25 = c10 = c5 = c1 = 0
    if coins > 25:
        c25, coins = divmod(coins, 25) 
    if coins > 10:
        c10, coins = divmod(coins, 10)
    if coins > 5:
        c5, coins = divmod(coins, 5)
    c1 = coins

    str = ''
    if c25 > 0:
        str += '%s枚25美分' % c25
    if c10 > 0:
        str += '%s枚10美分' % c10
    if c5 > 0:
        str += '%s枚5美分' % c5
    if c1 > 0:
        str += '%s枚1美分' % c1

    return str

ret = changeCoin(0.76)
print(ret)


def changeCoin(dollar):
    if dollar < 0 or dollar >1:
        return ('Please input less 1 dollar.')
    coins = int(100 * dollar)
    value = [25, 10, 5, 1]

    coin_num = []

    for v in value:
        coin_num.append(coins//v)   # 地板除
        coins = coins%v

    str = ''
    for k, v in zip(coin_num, value):   # 使用zip，不要转成dict
        if k > 0:
            str += '%s枚%s美分 ' % (k, v)

    return str

ret = changeCoin(0.76)
print(ret)
ret = changeCoin(0.3)
print(ret)


# 5-6
def calculator(expression):
    operator = ['+', '-', '*', '/', '%', '**']
    for op in operator:
        sp = expression.split(op)
        if len(sp) == 2:
            a, b = float(sp[0]), float(sp[1])
            if op == '+':
                return a + b
            if op == '-':
                return a - b  
            if op == '*':
                return a * b
            if op == '/':
                return a / b 
            if op == '%':
                return a % b
            if op == '**':
                return a ** b

                
ret = calculator('10 +  2')
print(ret)
ret = calculator('10 *   4.1')
print(ret)
ret = calculator('1  /   3')
print(ret)
ret = calculator('10 ** 4.1')
print(ret)

# 5-7
def tax(profit, rate=0.2):
    return profit * rate

print(tax(8000))

# 5-8
from math import pi

def calAreaVolume(para, type):
    if type == 0:   # square area
        result = para ** 2
    if type == 1:   # cube volume
        result = para ** 3
    if type == 2:   # circle area
        result = pi * para ** 2
    if type == 3:   # sphere volume
        result = 4/3 * pi * para ** 3

    return result

print(calAreaVolume(2, 0))
print(calAreaVolume(2, 1))
print(calAreaVolume(2, 2))
print(calAreaVolume(2, 3))

# 5-9
(a)为什么下面的例子里17+32等于49，而017+32等于47,017+032等于41？

Python2中 017是八56进制数，换算成十进制数为15
032同理

(b)为什么下面这个表达式我们得到的结果是134L而不是1342？
两个长整型数相加，l与数字1相似，提倡长整型用大写L
注意：python3 统一了整形和长整形，长整形已经不存在了。

# 5-10
def  centigrade(F):
    C = (F - 32) * (5 / 9)
    return C

print(centigrade(100))

# 5-11
even = [x for x in range(21) if x%2 == 0]
print(even)

odd = [x for x in range(21) if x%2 != 0]
print(odd)

取余运算是否有余数。

def foo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

print(foo(1, 3))
print(foo(3, 3))
print(foo(19, 3))
# print(foo(3, 0))

# 5-12
python3 sys模块没有maxint
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.
2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsi
lon=2.220446049250313e-16, radix=2, rounds=1)
>>> sys.int_info
sys.int_info(bits_per_digit=15, sizeof_digit=2)


# 5-13
def minutes(hour, min):
    return 60 * hour + min

print(minutes(3, 30))

# 5-14
def yearRate(dayRate):
    return (1 + dayRate) ** 365 - 1


print(yearRate(0.0001))


# 5-15
def commonDivisor(num1, num2):
    num = min(num1, num2)
    while num > 0:
        if (num1 % num == 0) and (num2 % num == 0):
            return(num)
        num = num - 1

print(commonDivisor(9, 90))


def commonMultipe(num1, num2):
    num = max(num1, num2)
    while True:
        if (num % num1 == 0) and (num % num2 == 0):
            return num
        num = num + 1

print(commonMultipe(3, 10))

# 5-16
def payMent(sum, monthly):
    moth, balance = divmod(sum, monthly)
    paid = [0]
    paid = paid + [monthly] * int(moth)
    if balance > 0:
        paid = paid + [balance]
    acu = 0
    print('Pymt#   Paid   Remaining')
    print('        Amount  Balance')
    print('-'*3 + ' '*3 + '-'*5 + ' '*5 + '-'*5)
    for i in range(len(paid)):
        acu = acu + paid[i]
        str = '%d' % i + ' '*4 + '$ %5.2f' % paid[i] + ' '*4 + '$ %5.2f' % (100-acu)
        print(str)


payMent(100.00, 20)
payMent(100.00, 16.13)

# 5-17
from random import randint

num = randint(1, 100)
print(num)

lst = []

for i in range(num):
    tmp = randint(0, pow(2, 31)-1)
    lst.append(tmp)

lst.sort()
print(lst)
