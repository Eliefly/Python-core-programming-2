# 第11章 函数和函数式编程

标签（空格分隔）： python-core-2

---
### 书中一些示例：

不带参数装饰器：
```
# filename: deco.py
from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print('[%s] %s() called' % (ctime(), func.__name__))
        return func()

    return wrappedFunc

@tsfunc
def foo():
    print('running foo()')

foo()

# output:
# [Thu Mar 30 09:38:56 2017] foo() called
# running foo()
```
任意类型任意个数的参数传递给任意函数对象。
```
# !/usr/bin/python3
# filename: testit.py
def testit(func, *kargs, **kwargs):

    try: 
        retval = func(*kargs, **kwargs)
        result = (True, retval)
    except Exception as diag:
        result = (False, diag)
    return result

def test():
    funcs = (int, float, set, list)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print('-'*20)
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)

            if retval[0]:
              
                print('%s(%s)' % (eachFunc.__name__, repr(eachVal)), retval[1])
            else:
                print('%s(%s) = FAILED' % (eachFunc.__name__, repr(eachVal)), retval[1])
if __name__ == '__main__':
    test()
```
简单的闭包示例：
```
def counter(start_at=0):
    count = [start_at]
    def incr():
        count[0] += 1
        return count[0]

    return incr

foo = counter(5)
print(foo())    # 6
print(foo())    # 7
foo2 = counter(100)
print(foo2())   # 101
print(foo())    # 8
```
代码的count做如下替换，运行时出错“UnboundLocalError: local variable 'num' referenced before assignment”。主要是`num += 1`即`num = num + 1`在`incr()`函数作用域内，认为在`incr()`函数作用域内先声明了`num`，没有向更外层的作用域`counter()`域内搜索`num`。
但是这个`num`是未初始化的，赋值表达式`num = num + 1`的右边`num`在未初始化时被引用了。上面示例通过`count[0] += 1`来访问到外层的`count`很巧妙。
```
def counter(start_at=0):
    num = start_at
    def incr():
        num += 1
        return num

    return incr
```
追踪闭包自由变量：
```
# !/usr/bin/python3.5

output = '<int %r id=%#0x val=%d'
w = x = y = z = 1

def f1():
    x = y = z = 2

    def f2():
        y = z = 3

        def f3():
            z = 4
            print(output % ('w', id(w), w)) # 全局变量
            print(output % ('x', id(x), x)) # 来自f1()的闭包变量
            print(output % ('y', id(y), y)) # 来自f2()的闭包变量
            print(output % ('z', id(z), z)) # 来自f3()的局部变量

        clo = f3.__closure__
        if clo:
            print('f3 closure vars:', [str(c) for c in clo])
        else:
            print('no f3 closure vars')
        f3()

    clo = f2.__closure__
    if clo:
        print('f2 closure vars:', [str(c) for c in clo])
    else:
        print('no f2 closure vars')
    f2()

clo = f1.__closure__
if clo:
    print('f1 closure vars:', [str(c) for c in clo])
else:
    print('no f1 closure vars')
f1()


# no f1 closure vars
# f2 closure vars: ['<cell at 0x0279A290: int object at 0x63153720>']
# f3 closure vars: ['<cell at 0x0279A290: int object at 0x63153720>', '<cell at 0x0279AA50: int object at 0x63153730>']
# <int 'w' id=0x63153710 val=1
# <int 'x' id=0x63153720 val=2
# <int 'y' id=0x63153730 val=3
# <int 'z' id=0x63153740 val=4
```
带参数的装饰器，参数决定哪一个闭包会被用。
```
# !/usr/bin/python3.5

from time import time

def logged(when):
    def log(f, *args, **kargs):
        print('''Called:
            function: %s
            args: %s
            kargs: %r''' % (f, args, kargs))

    def pre_logged(f):
        def wrapper(*args, **kargs):
            log(f, *args, **kargs)
            return f(*args, **kargs)
        return wrapper

    def post_logged(f):
        def wrapped(*args, **kargs):
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                log(f, *args, **kargs)
                print('time delta: %f' % (time() - now))

        return wrapped

    try:
        return {"pre": pre_logged, "post": post_logged}[when]
    except KeyError as e:
        raise ValueError(e) + 'must be "pre" or "post"'

@logged("post")
def hello(name):
    print('Hello, ', name)

hello("World!")

# Hello,  World!
# Called:
#             function: <function hello at 0x02611300>
#             args: ('World!',)
#             kargs: {}
# time delta: 0.000000

@logged("pre")
def hello(name):
    print('Hello, ', name)

hello("World!")

# Called:
#             function: <function hello at 0x029FE2B8>
#             args: ('World!',)
#             kargs: {}
# Hello,  World!
```
lambda 作用域，遵循和标准函数一样的作用于规则。
```
x = 10
def foo():
    y = 5
    bar = lambda: x+y
    print(bar())
    y = 8
    print(bar())

foo()

# 15
# 18

x = 10
def foo():
    y = 5
    bar = lambda y=y: x+y
    print(bar())
    y = 8
    print(bar())

foo()
# 外部y的值被传入lambda中“设置”，所以虽然其值在稍后改变了，但是lambda的定义没有变。
# 15
# 15
```
变量作用域，和C中差不多，函数内的局部变量在函数执行完后就销毁了。
```
# !/usr/bin/python3

j, k = 1, 2
def proc1():

    j, k = 3, 4
    print('j == %d and k == %d' % (j, k)) 
    k = 5

def proc2():

    j = 6
    proc1() # 3, 4
    print('j == %d and k == %d' % (j, k))   # 6, 7


k = 7
proc1() # 3, 4
print('j == %d and k == %d' % (j, k))   # 1, 7

j = 8
proc2()
print('j == %d and k == %d' % (j, k)) # 8, 7
```

11-3 函数。
在这个练习中，我们将实现max()和min()内建函数。
(a) 写分别带两个元素返回一个较大和较小元素，简单的max2()核min2()函数。他们应该可以用任意的python 对象运作。举例来说，max2(4,8)和min2(4,8)会各自每次返回8 和4。
(b) 创建使用了在a 部分中的解来重构max()和min()的新函数my_max()和my_min().这些函数分别返回非空队列中一个最大和最小值。它们也能带一个参数集合作为输入。用数字和字符串来测试你的解。
```
from functools import reduce

def max2(num1, num2):
    return num1 if num1 > num2 else num2

def min2(num1, num2):
    return num1 if num1 < num2 else num2

print(max2(4, 8))
print(min2(4, 8))
```
列表参数
```
def my_max(para):
    return reduce(max2, para)

def my_min(para):
    return reduce(min2, para)

print(my_max([1, 2, 5, 9]))
print(my_max('abcd'))

print(my_min([1, 2, 5, 9]))
print(my_min('abcd'))
```
非关键字可变长参数：
```
def my_max(*para):
    if len(para) > 0:
        ret = para[0]
    else:
        return None
    for ele in para:
        ret = max2(ret, ele)
    return ret

def my_min(*para):
    if len(para) > 0:
        ret = para[0]
    else:
        return None
    for ele in para:
        ret = min2(ret, ele)
    return ret

print(my_max(1, 3, 5, 9))
print(my_max('abcd', 'c', '123'))

print(my_min(1, 3, 5, 9))
print(my_min('abcd', 'c', '123'))
```
11–4. 返回值。
给你在5-13 的解创建一个补充函数。创建一个带以分为单位的总时间以及返回一个以小时和分为单位的等价的总时间。
```
def trans(min):
    h, m = divmod(min, 60)
    return(h, m)

print(trans(310))
```

def tax(profit, rate=0.2):
    return profit * rate
print(tax(8000))
11-5 默认参数。
更新你在练习 5-7 中创建的销售
```
def tax(profit, rate=0.2):
    return profit * rate
    
print(tax(8000))
```
11–6. 变长参数。
实现一个称为printf()的函数。有一个值参数，格式字符串。剩下的就是根据格式化字符串上的值，要显示在标准输出上的可变参数，格式化字符串中的值允许特别的字符串
格式操作指示符，如%d, %f, etc。提示：解是很琐碎的----无需实现字符串操作符功能性，但你需要显示用字符串格式化操作（%）
```
def printf(fmt, *varlist):  
    print(fmt % varlist)  
  
printf('%d-%d-%s', 2011, 3, '18')  
```
11–7. 用map() 进行函数式编程。
给定一对同一大小的列表， 如[1 ， 2 ， 3] 和['abc','def','ghi',....]，将两个标归并为一个由每个列表元素组成的元组的单一的表，以使我们的结果看起来像这样：{[(1, 'abc'), (2, 'def'), (3, 'ghi'), ...}.（虽然这问题在本质上和第六章的一个问题相似，那时两个解没有直接的联系）然后创建用zip 内建函数创建另一个解。
```
def myzip(lst1, lst2):
    return list(map(lambda x, y: (x, y), lst1, lst2))

print(myzip([1, 2, 3], ['abc', 'def', 'ghi']))
```

11–8. 用filer()进行函数式编程.
使用练习5-4 你给出的代码来决定闰年。更新你的代码一边他成为一个函数如果你还没有那么做的话。然后写一段代码来给出一个年份的列表并返回一个只有闰年的列表。然后将它转化为用列表解析
```
def isLeapyear(year):
    if (year%4 == 0 and year%100 != 0) or (year%400 ==0):
        return True
    else:
        return False

lst_year = [2000, 1998, 1990, 2004]

print(list(filter(isLeapyear, lst_year))) # filter
print([ele for ele in lst_year if isLeapyear(ele)]) # 列表解析式
```

11–9. 用reduce()进行函数式编程。
复习11.7.2 部分，阐述如何用reduce()数字集合的累加的代码。修改它，创建一个叫average()的函数来计算每个数字集合的简单的平均值。
```
from functools import reduce

def average(lst):
    sum = reduce(lambda x, y: x+y, lst)
    avg = sum / len(lst)
    return avg

print(average([1, 2, 3, 4, 5]))
```
11–10.用filter()进行函数式编程。在unix 文件系统中，在每个文件夹或者目录中都有两个特别的文件：'.'表示现在的目录，'..'表示父目录。给出上面的知识，看下os.listdir()函数的文档并描述这段代码做了什么：files = filter(lambda x: x and x[0] != '.', os. listdir(folder)) 
```
显示当前路径下的文件夹和文件，但不包含"."开头的文件夹或文件。
```

11–11.用map()进行函数式编程。
写一个使用文件名以及通过除去每行中所有排头和最尾的空白来“清洁“文件。在原始文件中读取然后写入一个新的文件，创建一个新的或者覆盖掉已存在的。给你的用户一个选择来决定执行哪一个。将你的解转换成使用列表解析。
```
def stripspace(filename1, filename2=None, create=0):

    if create == 0:
        filename = filename1
    else:
        filename = filename2

    stripline = lambda x: x.strip() + '\n'

    with open(filename1, 'r') as fobj1:
        lines = map(stripline, fobj1)
        lines = ''.join(lines)

    with open(filename, 'w') as fobj2:
        fobj2.write(lines)

stripspace('test.txt')   # 覆盖源文件
stripspace('test.txt', 'default.txt', 1)    # 新建文件
```
11–12. 传递函数。
给在这章中描述的testit()函数写一个姊妹函数。timeit()会带一个函数对象（和参数一起）以及计算出用了多少时间来执行这个函数，而不是测试执行时的错误。返回下面的状态：函数返回值，消耗的时间。你可以用time.clock()或者time.time()，无论哪一个给你提供了较高的精度。（一般的共识是在POSIX 上用time.time()，在win32 系统上用time.clock()）
注意：timeit()函数与timeit 模块不相关(在python2.3 中引入）
```
import time
def timeit(func, *kargs, **kwargs):
    start = time.clock()
    ret = func(*kargs, **kwargs)
    end = time.clock()
    inter = end - start
    return (ret, inter)

def sum(num):
    ret = 0
    for i in range(num):
        ret += i
    return ret

print(timeit(sum, 10000))
```
11–13.使用reduce()进行函数式编程以及递归。
在第8章中，我们看到N 的阶乘或者N!作为从1 到N 所有数字的乘积。
(a) 用一分钟写一个带x,y 并返回他们乘积的名为mult(x,y)的简单小巧的函数。
(b)用你在a 中创建mult()函数以及reduce 来计算阶乘。
(c)彻底抛弃掉mult()的使用，用lamda 表达式替代。
(d)在这章中，我们描绘了一个递归解决方案来找到N!用你在上面问题中完成的timeit()函数，并给三个版本阶乘函数计时(迭代的，reduce()以及递归）
```
from functools import reduce
import time

def factorial1(num):
    def mult(x, y):
        return x * y
    result = reduce(mult, range(1, num+1))
    return result

def factorial2(num):
    mult = lambda x, y: x * y
    result = reduce(mult, range(1, num+1))
    return result

def factorial3(num):
    if num > 1:
        result = num * factorial3(num-1)
    elif num == 1:
        result = 1

    return result


def timeit(func, *kargs, **kwargs):
    start = time.clock()
    ret = func(*kargs, **kwargs)
    end = time.clock()
    inter = end - start
    return (ret, inter)

print(timeit(factorial1, 100))
print(timeit(factorial2, 100))
print(timeit(factorial3, 100))
```
11–14. 递归。
我们也来看下在第八章中的Fibonacci 数字。重写你先前计算Fibonacci 数字的解(练习8-9）以便你可以使用递归。
```
def fibonacci(n):
    if n > 2:
        ret = fibonacci(n-1) + fibonacci(n-2)
    elif n == 1 or n == 2:
        ret = 1
    return ret

print(fibonacci(10))
```


11–15.递归。
重写练习6-5 的解，用递归向后打印一个字符串。用递归向前以及向后打印一个字符串。
```
def forward(a_str):
    if len(a_str) > 0:
        print(a_str[0])
        forward(a_str[1:])

def backward(a_str):
    if len(a_str) > 0:
        backward(a_str[1:])
        print(a_str[0])

forward('1234')
backward('1234')
```

11-16 更新easyMath.py。这个脚本，如例子11.1描绘的那样，以入门程序来帮助年轻人强化他们的数学技能。通过加入乘法作为可支持的操作来进一步提升这个程序。额外的加分：也加入除法，这比较难做些因为你要找到有效的整型除数。幸运地是，已经有代码来确定分子比分母大，所以不需要支持分数。
```
from operator import add, sub, mul, truediv
from random import randint, choice

ops = {'+': add, '-': sub, '*': mul, '/': truediv} # 直接加就可以吧。。。
MAXTRIES = 2

def doprob():
    op = choice('+-*/')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    ans = round(ans, 2) # 除法取2为小数点
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(input(pr)) == ans:
                print('correct')
                break
            if oops == MAXTRIES:
                print('answer\n%s%.2f' % (pr, ans))
            else:
                print('incorrect... try again')
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            
            print('invalid input...try again')
            break

def main():
    while True:
        doprob()
        try:
            opt = input('Again?[y]: ').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

main()
```
11–17.定义 
(a) 描述偏函数应用和currying 之间的区别。 
(b) 偏函数应用和闭包之间有什么区别？ 
(c) 最后，迭代器和生成器是怎么区别开的？ 
```
柯里化（Currying）是把接受多个参数的函数变换成接受一个单一参数(最初函数的第一个参数)的函数，并且返回接受余下的参数且返回结果的新函数的技术。
一个带n个参数的函数，柯里化后得到的函数固定第一个参数，返回一个带有n-1个参数的函数对象。
偏函数在柯里化上进行了泛化。它可以将函数的任意个（可以多个）参数固话，转化成一个带剩余参数的函数对象。简单来说偏函数的作用，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

from functools import partial

max10 = partial(max, 10, 100)
print(max10(1, 2, 3))   # 100
```
```
如果在一内部函数引用了更外部函数（不是全局）的参数和变量，那么这个内部函数就认为是闭包。简单如下，内部函数bar() 引用了更外部函数 foo() 内的局部变量 m，这样函数 bar() 就是一闭包。
def foo():
    m = 3
    def bar():
        n = 4
        ret = m + n
        return ret
    return bar

print(foo()())

感觉闭包更偏向函数程序内部结构的描述，偏函数更偏向结果函数的描述。通过闭包技术可以达成偏函数的效果。
def my_max(num, *args):    
    def max100(*args):
        ret = num
        for ele in args:
            if ret < ele:
                ret = ele
        return ret
    return max100

max100 = my_max(100)
print(max100(1, 2, 99))
```
```
可以直接作用于 for 循环的对象统称为可迭代对象：Iterable。可以使用 isinstance([obj], Iterable)判断一个对象是否是 Iterable 对象。
一类是集合数据类型，如list、tuple、dict、set、str等;
一类是generator，包括生成器和带 yield 的 generator function。
生成器包含在迭代器之内。生成器计算是惰性的，只有需要返回下一个数据时，它才会计算，可以使用 next() 计算下一元素。
```
11-18 同步化函数调用。复习下第6章中当引入浅拷贝和深拷贝时，提到的丈夫和妻子情形。他们共用了一个普通账户，同时对他们银行账户访问会发生不利影响。创建一个程序，让调用改变账户收支的函数必须同步。换句话说，在任意给定时刻只能有一个进程或者线程来执行函数。一开始你试着用文件，但真正的解决办法是用装饰器和threading或者mutex模块中的同步指令。看看18章获得更多灵感。
```
暂过
```
