#-*- coding: UTF-8 -*-
# !/usr/bin/python3.5

http://www.th7.cn/Program/Python/201607/905660.shtml



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


