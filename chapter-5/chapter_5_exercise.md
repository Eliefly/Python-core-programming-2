# 第5章 数字

---
另可参考：http://blog.csdn.net/reimuko/article/details/28100935
```
#-*- coding: UTF-8 -*-
# !/usr/bin/python3.5
```
##### 5-1 整型。讲讲Python普通整型和长整型的区别。
```
普通整型：
Python 中普通整型等价于C的（有符号）长整型。
在32位机器上，取值范围是 -2^31 ~ 2^31 - 1 ，也就是 -2 147 483 647 ~ 2 147 483 647；
在64位机器上使用64位编译器编译python，那么这个系统的整型将是64位；
长整型：
Python长整形类型能表达的数值仅仅与机器支持的（虚拟）内存大小有关，可以轻松表达很大的整形。这点和C或其它编译型语言的长整形类型有很大的不同。
```

##### 5-2 运算符
(a) 写一个函数，计算并返回两个数的乘积
(b) 写一段代码调用这个函数，并显示它的结果
```
def multipy(x, y):
    return x * y

print(multipy(3, 6))
```

##### 5-3 标准类型运算符. 
写一段脚本，输入一个测验成绩，根据下面的标准，输出他的评分成绩（A-F）。
A: 90–100
B: 80–89
C: 70–79
D: 60–69
F: <60
```
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
```

##### 5-4 取余。
判断给定年份是否是闰年。使用下面的公式：
一个闰年就是指它可以被4 整除，但不能被100 整除， 或者它既可以被4 又可以被100 整除。比如 1992，1996 和2000 年是闰年，但1967 和1900 则不是闰年。下一个是闰年的整世纪是 2400 年。
```
def isLeapyear(year):
    if (year%4 == 0 and year%100 != 0) or (year%400 ==0):
        return True
    else:
        return False

print(isLeapyear(2000))
print(isLeapyear(1900))
```

##### 5-5 取余。
取一个任意小于1 美元的金额，然后计算可以换成最少多少枚硬币。硬币有1美分，5 美分，10 美分，25 美分四种。1 美元等于100 美分。举例来说，0.76 美元换算结果
应该是 3 枚25 美分，1 枚1 美分。类似76 枚1 美分，2 枚25 美分+2 枚10 美分+1 枚5 美分+1枚1 美分这样的结果都是不符合要求的。
```
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
```
```
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
```

##### 5-6 算术。
写一个计算器程序 你的代码可以接受这样的表达式，两个操作数加一个运算符：N1 运算符 N2. 其中 N1 和 N2 为整数或浮点数，运算符可以是+, -, *, /, %, ** 分别表示
加法，减法， 乘法， 整数除，取余和幂运算。计算这个表达式的结果，然后显示出来。
提示：可以使用字符串方法 split(),但不可以使用内建函数 eval().
```
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
```
##### 5-7 营业税。
随意取一个商品金额，然后根据当地营业税额度计算应该交纳的营业税。 
```
def tax(profit, rate=0.2):
    return profit * rate

print(tax(8000))
```
##### 5-8 几何。计算面积和体积： 
(a) 正方形 和 立方体 
(b) 圆 和 球
```
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
```
##### 5-9
(a)为什么下面的例子里17+32等于49，而017+32等于47,017+032等于41？
(b)为什么下面这个表达式我们得到的结果是134L而不是1342？
```
Python2中 017是八56进制数，换算成十进制数为15
032同理

两个长整型数相加，l与数字1相似，提倡长整型用大写L
注意：python3 统一了整形和长整形，长整形已经不存在了。
```
##### 5-10  转换。
写一对函数来进行华氏度到摄氏度的转换。转换公式为 C = (F - 32) * (5 / 9) 应该在这个练习中使用真正的除法， 否则你会得到不正确的结果。
```
def  centigrade(F):
    C = (F - 32) * (5 / 9)
    return C

print(centigrade(100))
```
##### 5-11 取余。 
(a) 使用循环和算术运算，求出 0－20 之间的所有偶数 
(b) 同上，不过这次输出所有的奇数 
(c) 综合 (a) 和 (b)， 请问辨别奇数和偶数的最简单的方法是什么？ 
(d) 使用(c)的成果，写一个函数，检测一个整数能否被另一个整数整除。 先要求用户输 入两个数，然后你的函数判断两者是否有整除关系，根据判断结果分别返回 True 和 False; 
```
even = [x for x in range(21) if x%2 == 0]
print(even)

odd = [x for x in range(21) if x%2 != 0]
print(odd)

(c)取余运算是否有余数。

def foo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

print(foo(1, 3))
print(foo(3, 3))
print(foo(19, 3))
# print(foo(3, 0))
```
##### 5-12 系统限制。
写一段脚本确认一下你的 Python 所能处理的整数，长整数，浮点数和复数的范围。
```
python3 sys模块没有maxint
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.
2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsi
lon=2.220446049250313e-16, radix=2, rounds=1)
>>> sys.int_info
sys.int_info(bits_per_digit=15, sizeof_digit=2)
```

##### 5-13  转换。
写一个函数把由小时和分钟表示的时间转换为只用分钟表示的时间。 
```
def minutes(hour, min):
    return 60 * hour + min

print(minutes(3, 30))
```
##### 5-14 银行利息。写一个函数，以定期存款利率为参数， 假定该账户每日计算复利，请计算并返回年回报率。
```
def yearRate(dayRate):
    return (1 + dayRate) ** 365 - 1


print(yearRate(0.0001))
```

##### 5-15 最大公约数和最小公倍数。请计算两个整数的最大公约数和最小公倍数。
```
def commonDivisor(num1, num2):
    num = min(num1, num2)
    while num > 0:
        if (num1 % num == 0) and (num2 % num == 0):
            return(num)
        num = num - 1

print(commonDivisor(9, 90))
```
```
def commonMultipe(num1, num2):
    num = max(num1, num2)
    while True:
        if (num % num1 == 0) and (num % num2 == 0):
            return num
        num = num + 1

print(commonMultipe(3, 10))
```
##### 5-16 家庭财务。给定一个初始金额和月开销数， 使用循环，确定剩下的金额和当月的支出数， 包括最后的支出数。 Payment() 函数会用到初始金额和月额度， 输出结果应该类似下 面的格式（例子中的数字仅用于演示）： 
```
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
```
##### 5-17  随机数。熟读随机数模块然后解下面的题： 生成一个有 N 个元素的由随机数 n 组成的列表， 其中 N 和 n 的取值范围分别为： (1 < N <= 100), (0 <= n <= 2^31 -1)。然后再随机从这个列表中取 N (1 <= N <= 100)个随机数 出来， 对它们排序，然后显示这个子集。
```
from random import randint

num = randint(1, 100)
print(num)

lst = []

for i in range(num):
    tmp = randint(0, pow(2, 31)-1)
    lst.append(tmp)

lst.sort()
print(lst)
```




