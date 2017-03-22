# 第6章 序列：字符串、列表和元组 练习

```
#-*- coding: UTF-8 -*-
# !/usr/bin/python3.5
```
http://blog.csdn.net/reimuko/article/details/28113029



##### 6–1. 字符串.string 模块中是否有一种字符串方法或者函数可以帮我鉴定一下一个字符串是否是另一个大字符串的一部分?
```
string.find(str, beg=0, end=len(string))
string.index(str, beg=0, end=len(string))
可实现检测 str 是否包含在 string 中，若存在 find() 和 index() 方法返回str在string中的索引。若不存在 find() 返回 -1，index() 方法则是会报一个异常。
同样的还有
string.rfind(str, beg=0, end=len(string))
string.rindex(str, beg=0, end=len(string))
不过是从右边开始检测。
print('g1234567g'.find('g'))    # 0
print('g1234567g'.rfind('g'))   # 8
print('g1234567g'.index('g'))    # 0
print('g1234567g'.rindex('g'))   # 8

当然也可以用 in 来判断：
print('abc' in '123abc123') # True
```

##### 6–2. 字符串标识符. 修改例6-1 的idcheck.py 脚本,使之可以检测长度为一的标识符,并且可以识别Python 关键字,对后一个要求,你可以使用keyword 模块(特别是keyword.kelist)来帮你.
```
import string
import keyword

alphas = string.ascii_letters + '_'
nums = string.digits

def idcheck(myInput):
    alphasNum = alphas + nums

    if myInput in keyword.kwlist:
        print('[%s] is kewword in python.' % myInput)
        return False

    if len(myInput) == 0:
        print('Please input valid string')
        return False



    if len(myInput) == 1:
        if myInput in alphas:
            print('[%s] is an correct identifer' % myInput)
            return(True)

    if len(myInput) > 1:
        if myInput[0] not in alphas:
            print('Invalid: first symbol must be alphabetic.')
            ret = False
        else:
            for eachChar in myInput[1:]:
                if eachChar not in alphasNum:
                    print('Invalid: remaining symbols must be alphanumeric.')
                    ret = False
                    break
                else:
                    print('[%s] is an correct identifer' % myInput)
                    return(True)

print(idcheck('_'))
print(idcheck('_123'))
print(idcheck('if'))
print(idcheck('if3'))
```
##### 6–3. 排序
(a) 输入一串数字,从大到小排列之.
(b) 跟a 一样,不过要用字典序从大到小排列之.
```
#(a)
lst = [2, 4, 3, 5, 10]
lst = sorted(lst, reverse=True)
print(lst)  # [10, 5, 4, 3, 2]

lst = [2, 4, 3, 5, 10]
lst.sort(reverse=True)
print(lst)  # [10, 5, 4, 3, 2]
```
```
# (b)
lst = [2, 4, 3, 5, 10]
lst = sorted(lst, key=str, reverse=True)
print(lst)  # [5, 4, 3, 2, 10]

lst = [2, 4, 3, 5, 10]
lst.sort(key=str, reverse=True)
print(lst)  # [5, 4, 3, 2, 10]
```
```
>>> help(sorted)
Help on built-in function sorted in module builtins:

sorted(iterable, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customise the sort order, and the
    reverse flag can be set to request the result in descending order.
```
##### 6–4. 算术. 
更新上一章里面你的得分测试练习方案,把测试得分放到一个列表中去.你的代码应该可以计算出一个平均分,见练习2-9 和练习5-3.
```
def mark(scoreLst):
    mark = []
    sum = 0
    for score in scoreLst:
        sum += score
        if 90 <= score <= 100:
            mark.append('A')
        elif 80 <= score <= 89:
            mark.append('B')
        elif 70 <= score <= 79:
            mark.append('C')
        elif 60 <= score <= 69:
            mark.append('D')
        elif score < 60:
            mark.append('F')
    avg = float(sum/len(scoreLst))
    return (mark, avg)

scoreLst = [68, 90, 78, 83]
mark, avg = mark(scoreLst)
print(mark)
print(avg)
```
##### 6-5 字符串
(a)更新你在练习2-7 里面的方案,使之可以每次向前向后都显示一个字符串的一个字符.
(b)通过扫描来判断两个字符串是否匹配(不能使用比较操作符或者cmp()内建函数)。附加题：在你的方案里加入大小写区分.
(c)判断一个字符串是否重现(后面跟前面的一致).附加题：在处理除了严格的回文之外,加入对例如控制符号和空格的支持。
(d)接受一个字符,在其后面加一个反向的拷贝,构成一个回文字符串.

```
str = 'abcd'
n = 0
while n < len(str):
    print(str[n])
    n += 1

n = -1
while n > -len(str):
    print(str[n])
    n -= 1
```

```
# 应该是违反题意了，用了比较操作符。。
def compString(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    length = min(len1, len2)

    i = 0

    for i in range(length):
        if str1[i] != str2[i]:
            return ord(str1[i]) - ord(str2[i])

    if len1 == len2:
        return 0

    if len1 > len2:
        return ord(str1[i+1])

    if len1 < len2:
        return -ord(str2[i+1])


print(compString('abc', 'abc')) # 0
print(compString('abc', 'abcd')) # -100
print(compString('abcd', 'abc')) # 100
```

（c)看不懂题就，过。。。。。。
```
def reverseCopy(s):
    return s + s[::-1]

print(reverseCopy('abc'))
```
```
# code1
def stripBlank(s):
    pre = rear = 0
    for i in range(len(s)):
        if s[i] != ' ':
            pre = i
            break
    s = s[i:]

    i = -1
    while i > -len(s):
        if s[i] != ' ':
            rear = i
            break
        i -= 1
    s = s[0:(len(s)+rear+1)]
    return s


print(stripBlank('      ab    cd        '))
```

```
# code2
def stripBlank(s):
    if len(s) <= 0:
        return s
        
    # left strip
    while s[0] == ' ':
        s = s[1:len(s)]

    # right strip
    while s[-1] == ' ':
        s = s[0:len(s)-1]

    return s

print(stripBlank('   asdf asdf   '))
```
##### 6–7. 调试.看一下在例6.5 中给出的代码(buggy.py)
(a)研究这段代码并描述这段代码想做什么.在所有的(#)处都要填写你的注释.
(b)这个程序有一个很大的问题,比如输入6,12,20,30,等它会死掉,实际上它不能处理任何的偶数,找出原因.
(c)修正(b)中提出的问题.
```
'''
去除顺序列表中，能整除列表长度值的元素
'''

# 输入数字字符
# num_str = input('Enter a number: ')
num_str = '9'

# 将数字字符转化为数值
num_num = int(num_str)

# 构建列表，错误：range需要加 list() 工厂方法
fac_list = list(range(1, num_num+1))
print('BEFORE:', fac_list)

i = 0

while i < len(fac_list):
    if num_num % fac_list[i] == 0:
        # 错误：del一个列表元素后，列表的长度也会发生改变，在删除一个元素的时候，下标也会受到影响，会导致有的元素被遗漏
        del fac_list[i] 
        # 删除元素后相当于 i 不移动
        i = i - 1
    # 步长
    i = i + 1

print('AFTER: ', fac_list)
```

##### 6–8. 列表.
给出一个整数值,返回代表该值的英文，比如输入89 返回"eight-nine"。
附加题：能够返回符合英文语法规则的形式，比如输入“89”返回“eighty-nine”。本练习中的值限定在家0到1,000.
```
def transStrnum(input_str):
    word_lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    num_lst = []
    for num in input_str:
        num = int(num)
        num_lst.append(word_lst[num]) 
    output_str = '-'.join(num_lst)
    return output_str

print(transStrnum('1234567890'))  # one-three-eight
```

```
def transStrnum(input_str):

    num = int(input_str)
    assert num < 1000, 'Your input number out of range. Should be 0~1000'

    word_lst1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                'eleven', 'twevel', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    word_lst2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']  
    word_lst3 = 'hundred'  

    str_lst = []

    if num // 100 > 0:
        index, num = divmod(num, 100)
        str_lst.append(word_lst1[index])
        str_lst.append(word_lst3)

    if num > 19:
        index, num = divmod(num, 10)
        str_lst.append(word_lst2[index-2])
        if num > 0:
            str_lst.append(word_lst1[num])
    elif 0 < num < 19:
        str_lst.append(word_lst1[num])


    output_str = '-'.join(str_lst)
    return output_str

print(transStrnum('909'))  # nine-hundred-thirty-seven
```

##### 6–9. 转换.
为练习5-13 写一个姊妹函数, 接受分钟数, 返回小时数和分钟数. 总时间不变,并且要求小时数尽可能大.
```
def minutes(totalMinu):
    hour, minutes = divmod(totalMinu, 60)
    if hour > 0:
        str = '%s小时' % hour
    if minutes > 0:
        str += '%s分钟' % minutes
    return str

print(minutes(80))
```
##### 6–10.字符串.
写一个函数,返回一个跟输入字符串相似的字符串,要求字符串的大小写反转.比如,输入"Mr.Ed",应该返回"mR.eD"作为输出.
```
def reverseLetter(input_str):
    return input_str.swapcase()

print(reverseLetter('Mr.Ed'))   # mR.eD
```
```
def reverseLetter(input_str):
    output_srt = ''
    for s in input_str:
        if s.islower():
            output_srt += s.upper()
        if s.isupper():
            output_srt += s.lower()
    return output_srt


print(reverseLetter('Mr.Ed'))   # mReD
```

##### 6–11.转换
(a)创建一个从整数到IP 地址的转换程序,如下格式: WWW.XXX.YYY.ZZZ.
(b)更新你的程序,使之可以逆转换.
```
import socket
import struct
str_ip = socket.inet_ntoa(struct.pack('I', socket.htonl(1234)))
print(str_ip)   # 0.0.4.210
num_in = socket.ntohl(struct.unpack('I', socket.inet_aton(str('0.0.4.210')))[0])
print(num_in)   # 1234
```
```
# 网上参考代码
def int2ip(num):  
    ip = [(num >> i & 0xff) for i in range(24, -1, -8)]  
    return '%d.%d.%d.%d' % tuple(ip)  
  
def ip2int(ip):  
    temp = ip.split('.')  
    temp = [int(part) for part in temp]  
    temp = [temp[3-i//8] << i for i in range(24, -1, -8)]  
    return sum(temp)  

s = int2ip(1234)  
print(s)            # 0.0.4.210
print(ip2int(s))    # 1234 
```

##### 6–12.字符串
(a)创建一个名字为findchr()的函数,函数声明如下:
def findchr(string, char)
findchr()要在字符串string 中查找字符char,找到就返回该值的索引,否则返回-1.不能用string.*find()或者string.*index()函数和方法
(b)创建另一个叫rfindchr()的函数,查找字符char 最后一次出现的位置.它跟findchr()工作类似,不过它是从字符串的最后开始向前查找的.
(c)创建第三个函数,名字叫subchr(),声明如下:
def subchr(string, origchar, newchar)
subchr()跟findchr()类似,不同的是,如果找到匹配的字符就用新的字符替换原先字符.返回修改后的字符串.
```
def findchr(string, char):
    index = -1
    for i in range(len(string)):
        if string[i] == char:
            index = i
            break

    return index

print(findchr('012341', '1'))
```
```
def rfindchr(string, char):
    index = -1
    for i in range(len(string)):
        if string[i] == char:
            index = i
            # break

    return index

print(rfindchr('012341', '1'))
```

```
def subchr(string, origchr, newchar):
    output_str = ''
    for ch in string:
        if ch == origchr:
            output_str += newchar
        else:
            output_str += ch

    return output_str


print(subchr('12341561', '1', 'A'))
```

##### 6–13.字符串.
string 模块包含三个函数,atoi(),atol(),和atof(),它们分别负责把字符串转换成整数,长整型,和浮点型数字.从Python1.5 起,Python 的内建函数int(),long(),float()也可以做相同的事了,complex()函数可以把字符串转换成复数.(然而1.5 之前,这些转换函数只能工作于数字之上)
string 模块中并没有实现一个atoc()函数,那么你来实现一个,atoc(),接受单个字符串做参数输入,一个表示复数的字符串,例如,'-1.23e+4-5.67j',返回相应的复数对象.你不能用eval()函数,但可以使用complex()函数,而且你只能在如下的限制之下使用complex():complex(real,imag)的real 和imag 都必须是浮点值.

```
def atoc(input_str):
    input_str = input_str.strip()
    index_j = input_str.index('j')

    i = index_j - 1
    while i > 0:
        if input_str[i] in '+-':
            index_img = i
            break
        else:
            index_img = 0  # '5.67j  +1.23e+4'虚部在前，且没有‘+-’号。 
        i = i - 1
    str_img =input_str[index_img:index_j]
    # str_img = str_img.strip()

    str_real = input_str.replace(str_img+'j', '')
    # str_real = str_real.strip()

    ret = complex(float(str_real), float(str_img))
    return ret


print(atoc('  -1.23e+4  -5.67j '))
print(atoc('  -5.67j -1.23e+4 '))
print(atoc(' 5.67j  +1.23e+4  '))
```
##### 6–14.随机数.
设计一个"石头,剪子,布"游戏,有时又叫"Rochambeau",你小时候可能玩过,下面是规则.你和你的对手,在同一时间做出特定的手势,必须是下面一种手势:石头,剪子,布.胜利者从下面的规则中产生,这个规则本身是个悖论.
(a)布包石头.
(b)石头砸剪子,
(c)剪子剪破布.
在你的计算机版本中,用户输入她/他的选项,计算机找一个随机选项,然后由你的程序来决定一个胜利者或者平手.注意:最好的算法是尽量少的使用if 语句.
```
from random import randint

def Rochambeau(man):
    '''
    2: 石头，1：剪刀，0：布
    >0: man win
    <0: man lose
    0: draw
    '''
    assert 0 < man < 3, 'input man should in [0, 1, 2]'
    gesture = ['布', '剪刀', '石头']

    robot = randint(0, 2)
    ret = man - robot
    if ret == 2 or ret == -2:
        ret = -ret

    print('man: %s' % gesture[man])
    print('robot: %s' % gesture[robot])

    return ret

print(Rochambeau(2))
```

##### 6–15.转换
(a)给出两个可识别格式的日期,比如 MM/DD/YY 或者 DD/MM/YY 格式,计算出两个日期间的天数.
(b)给出一个人的生日,计算从此人出生到现在的天数,包括所有的闰月.
(c)还是上面的例子,计算出到此人下次过生日还有多少天.
```
from datetime import datetime

def intervalDays(time1, time2):
    '''
    时间格式选择 DD/MM/YY
    '''
    time1 = datetime.strptime(time1, '%d/%m/%Y')
    time2 = datetime.strptime(time2, '%d/%m/%Y')
    interval = (time1 - time2).days
    return abs(interval)

print(intervalDays('1/1/2016', '2/2/2017'))
```
```
from datetime import datetime

def bornDays(birthday):
    '''
    时间格式选择 DD/MM/YY
    '''
    birthday = datetime.strptime(birthday, '%d/%m/%Y')
    now = datetime.now()
    interval = (birthday - now).days
    return abs(interval)

print(bornDays('9/12/1990'))
```
```
from datetime import datetime

def nextBirthday(birthday):
    '''
    时间格式选择 DD/MM/YY
    '''
    birthday = datetime.strptime(birthday, '%d/%m/%Y')
    now = datetime.now()

    if (now.month > birthday.month) or (
        now.month == birthday.month and now.day > birthday.day):
        next_birth = datetime(now.year+1, birthday.month, birthday.day)
    else:
        next_birth = datetime(now.year, birthday.month, birthday.day)  

    interval = (next_birth - now).days
    return interval

print(nextBirthday('28/2/1990'))
```

##### 6–16.矩阵.
处理矩阵M 和N 的加和乘操作.

发现个问题，矩阵相加输出结果是`[[6, 3, 6], [6, 3, 6], [6, 3, 6]]`，不是预期的`[[4, 4, 4], [5, 6, 3], [6, 3, 6]]`。发现问题是初始化矩阵`output`时，`output = [output] * row_M`是浅式拷贝，导致矩阵每行的元素引用都是相同的。
```
def matrixAdd(M, N):
    row_M = len(M)
    row_N = len(N)
    col_M = len(M[0])
    col_N = len(N[0])
    assert (row_M == row_N) and (col_M == col_N)
    
    output = [0] * col_M
    output = [output] * row_M

    for i in range(row_M):
        for j in range(col_M):
            output[i][j] = M[i][j] + N[i][j]
    return output

M = [[1, 2, 3], [3, 4, 1], [1, 2, 3]]  
N = [[3, 2, 1], [2, 2, 2], [5, 1, 3]]  

print(matrixAdd(M, N)) # [[6, 3, 6], [6, 3, 6], [6, 3, 6]]
```
修改后的代码：
```
import copy

def matrixAdd(M, N):
    row_M = len(M)
    row_N = len(N)
    col_M = len(M[0])
    col_N = len(N[0])
    assert (row_M == row_N) and (col_M == col_N)

    # output = [0] * col_M
    # output = [output] * row_M   # 会产生浅式拷贝
    output = []
    for i in range(row_M):
        row = [0] * col_M
        output.append(row)

    for i in range(row_M):
        for j in range(col_M):
            output[i][j] = M[i][j] + N[i][j]
    return output

M = [[1, 2, 3], [3, 4, 1], [1, 2, 3]]  
N = [[3, 2, 1], [2, 2, 2], [5, 1, 3]]  

print(matrixAdd(M, N)) # [[4, 4, 4], [5, 6, 3], [6, 3, 6]]
```
```
def martixMultiply(M, N):
    row_M = len(M)
    row_N = len(N)
    col_M = len(M[0])
    col_N = len(N[0])
    assert col_M == row_N

    output = []
    for i in range(row_M):
        row = [0] * col_N
        output.append(row)

    for i in range(row_M):
        for j in range(col_N):
            op_m = [M[i][y] for y in range(col_M)]
            op_n = [N[x][j] for x in range(row_N)]
            tmp = [x*y for x, y in zip(op_m, op_n)]
            output[i][j] = sum(tmp)

    return output


M = [[1, 2], [3, 4], [7, 2]]  
N = [[3, 2, 1], [2, 2, 2]]  

print(martixMultiply(M, N)) # [[7, 6, 5], [17, 14, 11], [25, 18, 11]]
```

一更简洁方式，运用`map`高阶函数。
```
from operator import add, mul  
  
def matrix_add(M, N):  
    output = []  
    for i, item in enumerate(M):
        tmp = map(add, item, N[i])
        tmp = list(tmp)
        output.append(tmp)
    return output
  
def matrix_mul(M, N):  
    t = [[N[i][j] for i in range(len(N))] for j in range(len(N[0]))]
    output = [[sum(map(mul, iteM, iteN)) for iteN in t] for iteM in M]  
    return output  
  
M = [[1, 2, 3], [3, 4, 1], [1, 2, 3]]  
N = [[3, 2, 1], [2, 2, 2], [5, 1, 3]] 

print(matrix_add(M, N))

M = [[1, 2], [3, 4], [7, 2]]
N = [[3, 2, 1], [2, 2, 2]] 

print(matrix_mul(M, N)) # [[7, 6, 5], [17, 14, 11], [25, 18, 11]]
```

##### 6–17.方法.
实现一个叫myPop()的函数,功能类似于列表的pop()方法,用一个列表作为输入,移除列表的最新一个元素,并返回它.

```
def myPop(lst):
    assert len(lst) > 0, 'input list is empty'
    ret = lst[-1]
    del lst[-1]
    return ret

lst = [1, 2, 3]
print(myPop(lst))
print(lst)
print(myPop(lst))
print(lst)
print(myPop(lst))
print(lst)
```
##### 6-18 zip() 内建函数。
在6.13.2节里面关于zip() 函数的例子中，zip(fn, ln) 返回的是什么？
下面是zip的help信息。zip() 返回的对象用`__next__()`方法，这样看返回的对象是生成器对象，可以实现迭代。每次迭代得到的是一个tuple对象，迭代的最大长度由输入的序列参数中长度最短（类似木桶原理）的参数决定。
```
class zip(object)
 |  zip(iter1 [,iter2 [...]]) --> zip object
 |  
 |  Return a zip object whose .__next__() method returns a tuple where
 |  the i-th element comes from the i-th iterable argument.  The .__next__()
 |  method continues until the shortest iterable in the argument sequence
 |  is exhausted and then it raises StopIteration.
```
一码胜千语：
```
a_lst = (1, 2, 3, 4, 5)
b_lst = [7, 8, 9]
c_lst = ['a', 'b', 'c']

ret = zip(a_lst, b_lst, c_lst)

print(type(ret))    # <class 'zip'>

for i, j, k in ret:
    print(i, j, k)

# 1 7 a
# 2 8 b
# 3 9 c
```

##### 6–19.多列输出.
有任意项的序列或者其他容器,把它们等距离分列显示.由调用者提供数据和输出格式.例如,如果你传入100 个项并定义3 列输出,按照需要的模式显示这些数据.这种情况下,应
该是两列显示33 个项,最后一列显示34 个.你可以让用户来选择水平排序或者垂直排序.
```
def displayMuti(lst, num, mode='h'):
    avg, rest = divmod(len(lst), num)
    dis = [avg] * num
    dis[-1] += rest
    acu = [sum(dis[:i]) for i in range(1, num)]
    acu = [0] + acu
    if mode == 'h':
        for i in range(len(lst)):
            print('%s\t' % lst[i], end='')
            if i+1 == acu[1]:
                print('\n')
                if len(acu) > 2:
                    del acu[1]
    if mode == 'v':
        row_max = max(dis)
        row_avg = min(dis)
        for i in range(row_max):
            if i < row_avg:
                tmp = [lst[i+j] for j in acu]
                print('%s\t'*num % tuple(tmp))
            else:
                print('\t'*(num-1)+'%s' % lst[i+acu[-1]])

displayMuti(list(range(78)), 10, 'h')
print('\n')
displayMuti(list(range(78)), 10, 'v')
```





