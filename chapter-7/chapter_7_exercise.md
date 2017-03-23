# 第7章 映像和集合类型 

---
另可参考：http://blog.csdn.net/reimuko/article/details/28114593
```
# !/usr/bin/python3.5
# -*- coding:utf-8 -*- 
```

##### 7–1. 字典方法。
哪个字典方法可以用来把两个字典合并到一起？
```
# dict.update(dict2) 方法可实现。
a_dict = {'name': 'joey', 'age': 23}
b_dict = {'address': 'ShenZhen'}

a_dict.update(b_dict)
print(a_dict)   # {'address': 'ShenZhen', 'age': 23, 'name': 'joey'}
```

##### 7–2. 字典的键。我们知道字典的值可以是任意的Python 对象，那字典的键又如何呢？请试着将除数字和字符串以外的其他不同类型的对象作为字典的键，看一看，哪些类型可以，哪些不行？对那些不能作字典的键的对象类型，你认为是什么原因呢？

分别尝试用数字，字符串，列表，元组，字典作为字典的键值。其中，数字，字符串，元组可以作为字典键值，列表和字典则错误。**字典的健必须是可哈希的对象，包括所有不可变类型，和实现了__hash__()特殊方法的类。数字，字符串，元组这些符合要求。**因为解释器调用哈希函数，来根据键值计算得到数据的存储位置，如果键是可变的，那么位置的计算就会不可靠。  
```
a_dict = {123: 'test'}
a_dict = {'abc': 'test'}
a_dict = {(1, 2): 'test'}

a_dict = {[1, 2]: 'test'}   # unhashable type: 'list'
a_dict = {{123: 'test'}: 'test'}   # unhashable type: 'dict'
```

##### 7–3. 字典和列表的方法。
(a) 创建一个字典，并把这个字典中的键按照字母顺序显示出来。
(b) 现在根据已按照字母顺序排序好的键，显示出这个字典中的键和值。
(c)同(b),但这次是根据已按照字母顺序排序好的字典的值，显示出这个字典中的键和值。(注意：对字典和哈希表来说，这样做一般没有什么实际意义，因为大多数访问和排序(如果需要)都是基于字典的键，这里只把它作为一个练习。)
```
def displaysortkey(a_dict):
    key_lst = list(a_dict.keys())
    key_lst.sort(key=str)
    print(key_lst)
    
displaysortkey({1: 98, 2: 96, 'name': 'jack', (1, 2): 45, 'age': 32})
```
```
def displaysortkey(a_dict):
    key_lst = list(a_dict.keys())
    key_lst.sort(key=str)
    for key in key_lst:
        print(key, a_dict[key])

displaysortkey({1: 98, 2: 96, 'name': 'jack', (1, 2): 45, 'age': 32})
```
```
def displaysortvalue(a_dict):
    value_lst = list(a_dict.values())
    value_lst.sort(key=str)
    for value in value_lst:
        for key in a_dict:
            if a_dict[key] == value:
                print(key, value)
                del(a_dict[key])
                break

displaysortvalue({1: 98, 2: 96, 'name': 'jack', (1, 2): 45, 'age': 32})
```
##### 7-4. 建立字典。
给定两个长度相同的列表，比如说，列表[1, 2, 3,...]和['abc', 'def','ghi',...],用这两个列表里的所有数据组成一个字典，像这样：{1:'abc', 2: 'def', 3: 'ghi',...}
```
def zipdict(lst1, lst2):
    return dict(zip(lst1, lst2))

a_lst = [1, 2, 3, 4]    # 列表中如果有重复值，相同键值会覆盖
b_lst = ['abc', 'def', 'ghi', 'jkl']
print(zipdict(a_lst, b_lst))
```

##### 7–5. userpw2.py. 
下面的问题和例题7.1 中管理名字-密码的键值对数据的程序有关。
(a)修改那个脚本，使它能记录用户上次的登录日期和时间(用time 模块)，并与用户密码一起保存起来。程序的界面有要求用户输入用户名和密码的提示。无论户名是否成功登录，都应有提示，在户名成功登录后，应更新相应用户的上次登录时间戳。如果本次登录与上次登录在时间上相差不超过4 个小时，则通知该用户： “You already logged in at: <last_ login_timestamp>.”
(b) 添加一个“管理”菜单，其中有以下两项:(1)删除一个用户 (2)显示系统中所有用户的名字和他们的密码的清单。
(c) 口令目前没有加密。请添加一段对口令加密的代码(请参考crypt, rotor, 或其它加密模块)
(d) 为程序添加图形界面，例如，用Tkinter 写。
(e) 要求用户名不区分大小写。
(f) 加强对用户名的限制，不允许符号和空白符。
(g)合并“新用户”和“老用户”两个选项。如果一个新用户试图用一个不存在的用户名登录，
询问该用户是否是新用户，如果回答是肯定的，就创建该帐户。否则，按照老用户的方式登录。

安装 Tkinter
`sudo apt-get install python-tk`，装到 python2 下去了。。。
部分要求略过：
```
# -*- coding:utf-8 -*-

import time

from crypt import crypt
from hmac import compare_digest as compare_hash

db = {}
def newuser():
    prompt = 'login desired: '
    while True:
        name = input(prompt)
        if len(db) == 0:
            break

        flag = False
        for key in db:
            if key.lower() == name.lower(): # 用户名不区分大小写
                prompt = 'name taken, try another: '
                flag = True
                break
        if flag == False:
            break

    pwd = input('passwd: ')
    pwd_crp = crypt(pwd)    
    db[name] = pwd_crp # 密码以密文形式保存
    # 增加时间
    db[name + '_time'] = time.strftime("%Y-%m-%d %X", time.localtime()) # 格式化的时间字符串

def olduser():
    name = input('login: ')
    pwd = input('passwd: ')
    passwd = db.get(name)
    if compare_hash(passwd, crypt(pwd, passwd)): # 登录密码校验
        now = time.time()   # 当前时间戳（秒）
        last_str_time = db[name + '_time']  # 登录保存的字符串时间戳
        last_time = time.strptime(last_str_time, '%Y-%m-%d %X') # 转化为struct_time
        last_time = time.mktime(last_time)
        interval = last_time - now  # 间隔时间（秒）
        if interval/3600 < 4:
            print('You already logged in at %s' % last_str_time)
        else:
            db[name + '_time'] = time.strftime("%Y-%m-%d %X", time.localtime()) # 格式化的时间字符串
    else:
        print('login incorrect')

def showuser():
    print('用户信息: ')
    for k, v in db.items():
        print(k, v)

def showmenu():
    prompt = '''
    (N)ew User Login
    (E)xisting User Login
    (S)how User Info
    (Q)uit
    Enter choice:'''

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYour picked: [%s]' % choice)
            if choice not in 'neqs':
                print('invalid option, try again')
            else:
                chosen = True

        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
        if choice == 'e':
            olduser()
        if choice == 's':
            showuser()

if __name__ == '__main__':
    showmenu()
```
##### 7-6. 列表和字典。

创建一个简单的股票证券投资数据系统。其中应至少包含四项数据：股市行情显示器符号，所持有的股票，购买价格及当前价位 - 你可以随意添加其他数据项，比如收益率，
52 周最高指数、最低指数，等等。用户每次输入各列的数据构成一个输出行。每行数据构成一个列表。还有一个总列表，包括了所有行的数据。数据输入完毕后，提示用户选择一列数据项进行排序。把该数据项抽取出来作为字典的键，字典的值就是该键对应行的值的列表。提醒读者：被选择用来排序的数据项必须是非重复的键，否则就会丢失数据，因为字典不允许一个键有多个值。你还可以选择其他计算输出，比如，盈亏比率，目前证券资产价值等。

略

##### 7-7. 颠倒字典中的键和值。
用一个字典做输入，输出另一个字典，用前者的键做值，前者的值做键。
```
def intervalDict(dict1):
    dict2 = {}
    for k, v in dict1.items():
        dict2[v] = k

    return dict2

a_dict = {'name':'jack', 'age': 23, 'class': 3}
print(intervalDict(a_dict))
```

一句：
```
a_dict = {'name':'jack', 'age': 23, 'class': 3}
ret = dict(zip(a_dict.values(), a_dict.keys()))
print(ret)  # {3: 'class', 'jack': 'name', 23: 'age'}
```

##### 7-8. 人力资源。
创建一个简单的雇员姓名和编号的程序。让用户输入一组雇员姓名和编号。你的程序可以提供按照姓名排序输出的功能，雇员姓名显示在前面，后面是对应的雇员编号。附加
题：添加一项功能，按照雇员编号的顺序输出数据。
```

db = {}
def newEmployee():
    name = input('Please input employee name: ')
    number = input('Please input employee number: ')
    db[number] = name

def showInfo():
    lst_number = sorted(db.keys(), key=int)
    for key in lst_number:
        print(db[key], key)

def showmenu():
    prompt = '''
    (N)ew Employee
    (S)how Employee Info
    (Q)uit
    Enter choice:'''

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYour picked: [%s]' % choice)
            if choice not in 'neqs':
                print('invalid option, try again')
            else:
                chosen = True

        if choice == 'q':
            done = True
        if choice == 'n':
            newEmployee()
        if choice == 's':
            showInfo()


if __name__ == '__main__':
    showmenu()
```

##### 7-9. 翻译
(a) 编写一个字符翻译程序(功能类似于Unix 中的tr 命令)。我们将这个函数叫做tr()，它有三个字符串做参数: 源字符串、目的字符串、基本字符串，语法定义如下：
def tr(srcstr, dststr, string)
srcstr 的内容是你打算“翻译”的字符集合，dsrstr 是翻译后得到的字符集合，而string 是你打算进行翻译操作的字符串。举例来说，如果srcstr == 'abc', dststr == 'mno', string =='abcdef', 那么tr()的输出将是'mnodef'. 注意这里len(srcstr) == len(dststr).
在这个练习里，你可以使用内建函数chr() 和 ord(), 但它们并不一定是解决这个问题所必不可少的函数。
(b) 在这个函数里增加一个标志符参数，来处理不区分大小写的翻译问题。
(c)修改你的程序，使它能够处理删除字符的操作。字符串srcstr 中不能够映射到字符串dststr中字符的多余字符都将被过滤掉。换句话说，这些字符没有映射到dststr 字符串中的任何字符，因此就从函数返回的字符里被过滤掉了。举例来说：如果 srcstr == 'abcdef', dststr == 'mno',string == 'abcdefghi', 那么tr()将输出'mnoghi'. 注意这里len(srcstr) >= len(dststr).
```
def tr(srcstr, dststr, string, flag=False):
    len_src = len(srcstr)
    len_dst = len(dststr)

    # len(srcstr) >= len(dststr)的情况
    if len_src > len_dst:
        dststr = list(dststr) + ['']*(len_src - len_dst)
    tr_dict = dict(zip(srcstr, dststr))

    out_str = ''

    if flag == False:   # 不区分大小写
        for ch in string:
            if ch.lower() in tr_dict:   
                out_str += tr_dict[ch.lower()]
            elif ch.upper() in tr_dict:
                out_str += tr_dict[ch.upper()]
            else:
                out_str += ch
    elif flag == True:   # 不区分大小写
        for ch in string:
            if ch in tr_dict:   
                out_str += tr_dict[ch]
            else:
                out_str += ch

    return out_str

print(tr('abCdef', 'Mon', 'aBcdefghi', True))   # MBcghi
print(tr('abCdef', 'Mon', 'aBcdefghi', False))  # Monghi
```


##### 7–10. 加密。
(a) 用上一个练习的思路编写一个"rot13"翻译器。"rot13"是一个古老而又简单的加密方法，它把字母表中的每个字母用其后的第13 个字母来代替。字母表中前半部分字母将被映射到后半部分，而后半部分字母将被映射到前半部分，大小写保持不变。举例来说，'a'将被替换为'n','X'将被替换为'K'; 数字和符号不进行翻译。
(b)在你的解决方案的基础上加一个应用程序，让它提示用户输入准备加密的字符串(这个算法同时也可以对加密后的字符串进行解密)，如下所示:
```
% rot13.py
Enter string to rot13: This is a short sentence. Your string to en/decrypt was: [This
is a short sentence.].
The rot13 string is: [Guvf vf n fubeg fragrapr.].
%
% rot13.py
Enter string to rot13: Guvf vf n fubeg fragrapr. Your string to en/decrypt was: [Guvf
vf n fubeg fragrapr.].
The rot13 string is: [This is a short sentence.].
```
```
from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase

def tr(srcstr, dststr, string, flag=False):
    len_src = len(srcstr)
    len_dst = len(dststr)

    # len(srcstr) >= len(dststr)的情况
    if len_src > len_dst:
        dststr = list(dststr) + ['']*(len_src - len_dst)
    tr_dict = dict(zip(srcstr, dststr))

    out_str = ''

    if flag == False:   # 不区分大小写
        for ch in string:
            if ch.lower() in tr_dict:   
                out_str += tr_dict[ch.lower()]
            elif ch.upper() in tr_dict:
                out_str += tr_dict[ch.upper()]
            else:
                out_str += ch
    elif flag == True:   # 不区分大小写
        for ch in string:
            if ch in tr_dict:   
                out_str += tr_dict[ch]
            else:
                out_str += ch

    return out_str


def rot13(tr_str):
    lowercase_tr = lowercase[13:26] + lowercase[0:13]
    uppercase_tr = uppercase[13:26] + uppercase[0:13]

    print('Your string to en/decrypt was: [%s]' % tr_str)
    ret = tr(lowercase+uppercase, lowercase_tr+uppercase_tr, tr_str, True)
    print('the rot13 string is: [%s]' % ret)


a_str = 'This is a short sentence.'
rot13(a_str)
a_str = 'Guvf vf n fubeg fragrapr.'
rot13(a_str)

# Your string to en/decrypt was: [This is a short sentence.]
# the rot13 string is: [Guvf vf n fubeg fragrapr.]
# Your string to en/decrypt was: [Guvf vf n fubeg fragrapr.]
# the rot13 string is: [This is a short sentence.]
```
##### 7-11 定义。什么组成字典中合法的键？举例说明字典中合法的键和非法的键？
参见7-2

##### 7-12 定义。
(a)在数学上，什么是集合？
(b)在python中，关于集合类型的定义是什么？
数学上，由一个或多个确定的元素所构成的整体叫做集合。集合就是“确定的一堆东西”。集合里的“东西”，叫作元素。
Python把集合的概念引入到它的集合类型对象里。**集合对象是一组无序排列的可哈希的值**。（集合中的元素可以做字典的键。）

7–13. 随机数。
修改练习5-17 的代码：使用random 模块中的randint()或randrange()方法生成一个随机数集合：从0 到9(包括9)中随机选择，生成1 到10 个随机数。这些数字组成集合
A(A 可以是可变集合，也可以不是)。同理，按此方法生成集合B。每次新生成集合A 和B 后，显示结果 A | B 和 A & B
```
from random import randint

lstA = [randint(1, 10) for i in range(randint(1, 10))]
lstB = [randint(1, 10) for i in range(randint(1, 10))]

setA = set(lstA)
setB = set(lstB)

print('lstA: ', lstA)
print('lstB: ', lstB)

print('A: ', setA)
print('B: ', setB)

print('A|B: ', setA|setB)
print('A&B: ', setA&setB)
```

##### 7–14. 用户验证。
修改前面的练习，要求用户输入 A | B 和 A & B 的结果，并告诉用户他(或她)的答案是否正确，而不是将 A | B 和 A & B 的结果直接显示出来。如果用户回答错误，允许他(或她)修改解决方案，然后重新验证用户输入的答案。如果用户三次提交的答案均不正确，程序将显示正确结果。附加题：运用你关于集合的知识， 创建某个集合的潜在子集，并询问用户此潜在子集是否真是该集合的子集，要求和主程序一样有显示更正和答案的功能。
```
from random import randint

def str2set(a_str):
    union_set = a_str.split(',')
    ret = set(map(int, union_set))
    return ret

def solveSet():
    lstA = [randint(1, 10) for i in range(randint(1, 10))]
    lstB = [randint(1, 10) for i in range(randint(1, 10))]

    setA = set(lstA)
    setB = set(lstB)
    print('A: ', setA)
    print('B: ', setB)

    union_set = setA|setB
    inter_set = setA&setB

    for i in range(3):
        # 手动输入结果，','分隔
        # 或者可以借助eval(),a_set = eval(input('Please input A|B result: ')),输入则直接输入{1, 2, 3}样式输入
        a_str = input('Please input A|B result: ') 
        a_set = str2set(a_str)
        b_str = input('Please input A&B result: ')
        b_set = str2set(b_str)

        if union_set == a_set and inter_set == b_set:
            print('Your answer is correct!')
            break
        else:
            if i == 2:
                print('Your answer is wrong! The correct result is: \n')
                print('A|B: ', union_set)
                print('A&B: ', inter_set)
            elif i != 2:
                print('\nYour answer is wrong! Please input again!\n')


if __name__ == '__main__':
    solveSet()
```
判断子集的方法：
```
>>> set1 = {1, 2, 3}
>>> set2 = {1, 2, 4, 5, 3}
>>> set1 <= set2
True
```


##### 7–15. 编写计算器。
这个练习取材于http://math.hws.edu/ 在线免费Java 教材中的练习12.2。编写一个程序允许用户选择两个集合:A 和B, 及运算操作符。例如，in, not in, &, |, ^, <,<=, >, >=, ==, !=, 等. (你自己定义集合的输入语法，它们并不一定要像Java 示例中那样用方括号括住。)解析输入的字符串，按照用户选择的运算进行操作。你写的程序代码应该比Java 版本的
该程序更简洁。

自己一时没看懂题意，参考网络代码：
```
def compute(a, b, op):  
    foo = {}  
    foo['in'] = lambda x, y: x in y  
    foo['not in'] = lambda x, y: x not in y  
    foo['&'] = lambda x, y: x & y  
    foo['|'] = lambda x, y: x | y  
    foo['^'] = lambda x, y: x ^ y  
    foo['<'] = lambda x, y: x < y  
    foo['<='] = lambda x, y: x <= y  
    foo['>'] = lambda x, y: x > y  
    foo['>='] = lambda x, y: x >= y  
    foo['=='] = lambda x, y: x == y  
    foo['!='] = lambda x, y: x != y  
    foo['-'] = lambda x, y: x - y  
    if op not in foo:  
        return None  
    return foo[op](a, b)  
  
def main():  
    ls1 = eval(input('A: '))  
    ls2 = eval(input('B: '))  
    a = set(ls1)  
    b = set(ls2)  
    op = input('operator: ')  
    print(compute(a, b, op))  
  
if __name__ == '__main__':  
    main()  

# $ python3 run.py 
# A: {1, 2, 3}   
# B: {2, 3, 4, 5}
# operator: |
# {1, 2, 3, 4, 5}
```
