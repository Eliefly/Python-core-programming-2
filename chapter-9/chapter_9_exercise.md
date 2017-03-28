# 第9章 文件和输入输出


---

9–1. 文件过滤.
显示一个文件的所有行, 忽略以井号( # )开头的行. 这个字符被用做Python , Perl, Tcl, 等大多脚本文件的注释符号.附加题: 处理不是第一个字符开头的注释.
```
def filteranno(filename):
    with open(filename, 'r') as fobj:
        for eachline in fobj:
            if not eachline.lstrip().startswith('#'):
                print(eachline, end='')
    fobj.close()

filteranno('test.py')
```

9–2. 文件访问.
提示输入数字 N 和文件 F, 然后显示文件 F 的前 N 行.
```
def display(num, filename):
    i = 0
    with open(filename, 'r') as fobj:
        for eachline in fobj:
            if i < num:
                print(eachline, end='')
            i += 1

    fobj.close()

display(7, 'test.py')
```
9–3. 文件信息.
提示输入一个文件名, 然后显示这个文本文件的总行数.
```
def filerow(filename):
    row = 0
    with open(filename, 'r') as fobj:
        for eachline in fobj:
            row += 1
    fobj.close()
    return(row)

print(filerow('test.py'))
```
9–4. 文件访问.
写一个逐页显示文本文件的程序. 提示输入一个文件名, 每次显示文本文件的 25 行, 暂停并向用户提示"按任意键继续.", 按键后继续执行.
```
def display(filename, page=5):
    row = 0
    with open(filename, 'r') as fobj:
        for eachline in fobj:
            if row < page:
                print(eachline, end='')
                row += 1
            elif row == page:
                input('Please press any key to continue')   # 任意键 + 回车
                print(eachline, end='')
                row = 1
    fobj.close()

print(display('test.py'))
```
```
def display(filename, page=5):
    with open(filename, 'r') as fobj:
        for i, eachline in enumerate(fobj):
            print(eachline, end='')
            if (i + 1) % page == 0:
                input('Press any key to continue...')

    fobj.close()

print(display('test.py'))
```

9–6. 文件比较.
写一个比较两个文本文件的程序. 如果不同, 给出第一个不同处的行号和列号.
```
def diffstr(str1, str2):
    col = []
    i = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            col.append(i)
        i += 1
    len1 = len(str1)
    len2 = len(str2)
    max_len = max(len1, len2)
    min_len = min(len1, len2)
    col += list(range(min_len, max_len))
    return(col)

def difffile(file1, file2):
    fobj1 = open(file1, 'r')
    fobj2 = open(file2, 'r')

    lines1 = fobj1.readlines()
    lines2 = fobj2.readlines()

    len1 = len(lines1)
    len2 = len(lines2)

    if len1 > len2:
        lines2 += [''] * (len1 - len2)
    if len1 < len2:
        lines1 += [''] * (len2 - len1)

    row = 1 # 从第1行开始，没有第0行
    lst_row_col = []
    for line1, line2 in zip(lines1, lines2):
        if line1 != line2:
            col = diffstr(line1, line2)
            lst_row_col.append([row, col])
        row += 1

    return lst_row_col

print(difffile('test1.txt', 'test2.txt'))
```

9–7. 解析文件.
Win32 用户: 创建一个用来解析 Windows .ini 文件的程序. POSIX 用户:创建一个解析 /etc/serves 文件的程序. 其它平台用户: 写一个解析特定结构的系统配置文件的程序.
解析成啥样？
```
def parseconfig(filename):
    with open(filename, 'r') as fobj:
        for line in fobj:
            splitline = line.split(':')
            print(splitline)

parseconfig('/etc/passwd')
```
9–8. 模块研究.
提取模块的属性资料. 提示用户输入一个模块名(或者从命令行接受输入).然后使用 dir() 和其它内建函数提取模块的属性, 显示它们的名字, 类型, 值.
```
name = 'datetime'
obj = __import__(name)
ls = dir(obj)
for item in ls:
    print('name', item)
    print('type', type(getattr(obj, item)))
    print('value', getattr(obj, item))
```

9–9. Python 文档字符串.
进入 Python 标准库所在的目录. 检查每个 .py 文件看是否有__doc__ 字符串, 如果有, 对其格式进行适当的整理归类. 你的程序执行完毕后, 应该会生成一个漂亮的清单. 里边列出哪些模块有文档字符串, 以及文档字符串的内容. 清单最后附上那些没有文档字符串模块的名字.附加题: 提取标准库中各模块内全部类(class)和函数的文档.

 Python 标准库所在的目录的所有'*.py'文件有点多。。。
```
# -*- coding: utf-8 -*-

import os

def tracedir(dirname, py_file):
    '''
    找出指定目录下所有的'*.py'文件
    '''
    lsdir = os.listdir(dirname)
    py_file1 = set()
    for item in lsdir:
        # 分离的目录和内容组合成一个路径名
        fullpath = os.path.join(dirname, item)
        if os.path.isfile(fullpath):
            if os.path.splitext(item)[1] == '.py':
                py_file.add(fullpath)
        elif os.path.isdir(fullpath):   # 是否是目录
            py_file1 = tracedir(fullpath, py_file)

    py_file = py_file1 | py_file
    return py_file
    
py_file = set()
libdir = 'C:\Program Files\Python\Python35-32\Lib'
all_file = tracedir(libdir, py_file)
```
只考虑当前目录下的'*.py'文件，不考虑子路径下的
```
# -*- coding: utf-8 -*-

import os
from functools import reduce

def findpyfile(dirname):
    lsdir = os.listdir(libdir)
    py_file = []
    for item in lsdir:
        if os.path.splitext(item)[1] == '.py':
            py_file.append(os.path.join(dirname, item))

    return py_file

def docstring(py_file):
    db = {}
    for item in py_file:
        with open(item, encoding='utf-8') as fobj:
            doc = ''
            start = False
            for line in fobj:  
                if line.strip().startswith('"""') and not start: 
                    start = True 
                    doc += line 
                    if doc.strip().endswith('"""') and len(doc.strip()) > 3:  
                        start = False  
                        break  
                elif line.strip().endswith('"""'):  
                    start = False  
                    doc += line  
                    break  
                elif start:  
                    doc += line  
        if len(doc) > 0:
            db[os.path.split(item)[1]] = doc
    return db


libdir = 'C:\Program Files\Python\Python35-32\Lib'
py_file = findpyfile(libdir)
db = docstring(py_file)

for k, v in db.items():
    print('%s: \n\n\n %s' % (k, v))
    print('*'*40)
```

9-10 家庭理财。创建一个家庭理财程序。你的程序需要处理储蓄、支票、金融市场、定期存款等多种账户。为每种账户提供一个菜单操作界面，要有存款、取款、借、贷、等操作。另外还要提供一种取消操作的选项。用户退出这个程序时相关数据应该保存到文件里去（出于备份的目的，程序执行过程中也要备份）


9–11. Web 站点地址.
a) 编写一个 URL 书签管理程序. 使用基于文本的菜单, 用户可以添加, 修改或者删除书签数据项. 书签数据项中包含站点的名称, URL 地址, 以及一行简单说明(可选). 另外提供检索功能,可以根据检索关键字在站点名称和 URL 两部分查找可能的匹配. 程序退出时把数据保存到一个磁盘文件中去; 再次执行时候加载保存的数据.
b)改进 a) 的解决方案, 把书签输出到一个合法且语法正确的 HTML 文件(.html 或 htm )中,这样用户就可以使用浏览器查看自己的书签清单. 另外提供创建"文件夹"功能, 对相关的书签进行分组管理.
附加题: 请阅读 Python 的 re 模块了解有关正则表达式的资料, 使用正则表达式对用户输入的 URL 进行验证.
参考：

分类的"文件夹"功能没实现。
```
# -*- coding: utf-8 -*-
import re

url_db = dict()
index = 0
lst_index = list()

def isurl(url):
    # 简单的验证URL的正确性
    pattern = re.compile(r'^(http|HTTP|Http)s?\:[\w\/\.\&]+$') # url: http[s]:[字母，数字，/, ., &]
    ret = re.match(pattern, url)
    if ret is not None:
        return True

def inserturl():
    global index
    global lst_index
    name = input('Please input URL name: ')
    while True:
        try:
            url = input("Please input an correct URL or 'q' to quit: ")
            if url != 'q':
                if not isurl(url):
                    print('Invalid URL, try again.')
                    continue
                else:
                    break
        except (EOFError, KeyboardInterrupt):
            url = 'q' 

        if url == 'q':
            return None

    remarks = input('Please input URL remarks: ')
    category = input("Please input URL's category: ")

    url_db[index] = [name] + [url] + [remarks] + [category]
    index = index + 1
    lst_index = sorted(url_db.keys())   # 按顺序记录索引



def modifyurl():
    prompt = '''
    0 -- modifly url name
    1 -- modify url
    2 -- nodify remarks
    3 -- modify url category
    q -- quit modify

    your choice: '''

    showurl()
    to_modify = int(input('Please input an index of URL to be modify: '))
    if to_modify not in url_db:
        print('The URL that you want modify is not exist.')
        return None
    else:
        print('Enter modify mode:')

    while True:
        print('\nCurrent content:\n')
        print(url_db[to_modify])
        label = input(prompt).strip()[0]
        if label not in '0123q':
            print('Your choice is invalid, try again.')
            continue
        elif label in '0123':
            label = int(label)
            url_db[to_modify][label] = input('Please input content: ')
        elif label == 'q':
            break


def deleteurl():
    showurl()
    to_delete = int(input('Please input an index of URL to be delete: '))
    if to_delete not in url_db:
        print('The URL that you want delete is not exist.')
        return None
    else:
        url_db.pop(to_delete)
        print('Delete URL is success!!!')


def findurl():
    search_word = input('Please input word for search: ')
    for i in lst_index:
        # 简单的检索
        if search_word in url_db[i][0] or search_word in url_db[i][1]:
            print('[%s]:\t%s' % (i, url_db[i]))
        else:
            print('No suitable results!!!')


def showurl():
    if len(lst_index) > 0:
        for i in lst_index:
            print('[%s]:\t%s' % (i, url_db[i]))
    else:
        print('URL DB is empty!!!')


def exportHTML():
    '''导出到HTML文件'''
    str_begin = '''
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>

<table  cellspacing="50">
    <tr>
        <th>name</th>
        <th>remarks</th>
        <th>category</th>
    </tr>
    '''
    str_tail = '''
</table>

</body>
</html>
    '''

    str1 = ''
    for i in lst_index:
        tmp = '''
    <tr>
        <td><a href="%s">%s</a></td>
        <td>%s</td>
        <td>%s</td>
    </tr>
        ''' % (url_db[i][1], url_db[i][0], url_db[i][2], url_db[i][3])
        str1 += tmp

    lst_str = [str_begin] + [str1] + [str_tail]

    out_str = ''.join(lst_str)
    with open('URL.html', 'w', encoding='utf-8') as fobj:
        fobj.write(out_str)
    fobj.close()


CMDs = {'i': inserturl, 'm': modifyurl, 'd': deleteurl, 'f': findurl, 's': showurl, 'e': exportHTML}


def showmenu():
    prompt = '''
    (I)nsert
    (M)odify
    (D)elete
    (F)ind
    (S)how
    (E)xport as HTML
    (Q)uit

    Enter your choice: '''

    while True:
        while True:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'

            print('\nYour picked: [%s]' % choice)

            if choice not in 'imdfseq':  
                print('Invalid option, try again.')
            else:   # 正确的命令项，跳出输入命令循环
                break

        if choice == 'q':
            break       # 退出程序

        CMDs[choice]()

if __name__ == '__main__':
    showmenu()
```
HTML文件示例：
```

<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>

<table  cellspacing="50">
    <tr>
        <th>name</th>
        <th>remarks</th>
        <th>category</th>
    </tr>
    
    <tr>
        <td><a href="http://wwww.baidu.com">百度</a></td>
        <td>全球最大的中文搜索引擎、致力于让网民更便捷地获取信息，找到所求。</td>
        <td>搜索</td>
    </tr>
        
    <tr>
        <td><a href="https://cn.bing.com/">必应</a></td>
        <td>微软必应搜索是国际领先的搜索引擎,为中国用户提供网页、图片、视频、词典、翻译、资讯、地图等全球信息搜索服务。</td>
        <td>搜索</td>
    </tr>
        
    <tr>
        <td><a href="https://www.cnblogs.com/">博客园</a></td>
        <td>博客园创建于2004年1月，博客园诞生于江苏扬州这样一个IT非常落后的小城市。</td>
        <td>博客</td>
    </tr>
        
    <tr>
        <td><a href="http://www.csdn.net/">CSDN</a></td>
        <td>中国最大的IT社区和服务平台,为中国的软件开发者和IT从业者提供知识传播、职业发展、软件开发等全生命周期服务。</td>
        <td>博客</td>
    </tr>
        
</table>

</body>
</html>
```
9-12 用户名和密码。回顾练习7-5，修改代码使之可以支持“上次登录时间”。请参阅time模块中的文档了解如何记录用户上次登录的时间。另外提供一个系统管理员，他可以导出所有用户的用户名，密码（如需要可以加密），以及上次登录时间。
a）数据应保存在磁盘中，使用冒号：分隔，一次写入一行，例如“Joe：boohoo：953176591.145，文件中数据的行数应该等于你系统上的用户数。
b）进一步改进你的程序，不再一次写入一行，而使用pickle模块保存整个数据对象。请参阅pickle模块的文档了解如何序列化/扁平化对象，以及如何读写保存的对象。一般来说，这个解决方案的代码行数要比a）少；
c）使用shelve模块替换pickle模块，由于可以省去一些维护代码，这个解决方案的代码比b）的更少。
```
暂略
```

9–13. 命令行参数
a) 什么是命令行参数, 它们有什么用?
b) 写一个程序, 打印出所有的命令行参数.
``` 
# 命令行参数是调用某个程序时除程序名以外的其他参数，这些参数和程序的文件名一同被输入。

import sys

def printargv():
    for item in sys.argv:
        print(str(item))

printargv()

```

9-14 记录结果。修改你的计算器程序（练习5-6）使之接受命令行参数。例如`$ calc.py 1 + 2` 只输出计算结果。另外，把每个表达式和它的结果写入到一个磁盘文件中，当使用下面的命令时`$ calc.py print` 会把记录的内容显示到屏幕上，然后重置文件。这里是样例展示：
```
$ calc.py 1 + 2
3
$ calc.py 3 ^ 3
27
$ calc.py print
1 + 2
3
3 ^ 3
27
$ calc.py print
$ 
```

```
# -*- coding: utf-8 -*-
from sys import argv

def calc():
    filename = 'out.txt'
    len_argv = len(argv)
    # print(argv)
    if len_argv == 4:
        express = ' '.join(argv[1:])
        print(express)
        ret = eval(express)
        with open(filename, 'a') as fobj:
            fobj.write(express + '\n')
            fobj.write(str(ret) + '\n')
        print(ret)
    elif len_argv == 2 and argv[1] == 'print':
        with open(filename, 'r') as fobj:
            for line in fobj:
                print(line, end='')
                fobj.flush()
        with open(filename, 'w') as fobj:            
            fobj.write('')

calc()

# $ python3 calc.py 1 - 13
# $ python3 calc.py 1 + 1
# $ python3 calc.py print
```
9–15. 复制文件. 提示输入两个文件名(或者使用命令行参数). 把第一个文件的内容复制到第二个文件中去.
```
# -*- coding: utf-8 -*-

def copyfile(file1, file2):
    with open(file1, 'r') as fobj1:
        with open(file2, 'w') as fobj2:
            for line in fobj1:
                fobj2.write(line)
                
copyfile('out.txt', 'out1.txt')
```
9–16. 文本处理. 
人们输入的文字常常超过屏幕的最大宽度. 编写一个程序, 在一个文本文件中查找长度大于 80 个字符的文本行. 从最接近 80 个字符的单词断行, 把剩余文件插入到下一行处.程序执行完毕后, 应该没有超过 80 个字符的文本行了.
```
# -*- coding:utf-8 -*-

def reshape(filename, num):
    '''
    filename: 文件名
    num: 每行num个字符
    '''
    with open(filename, 'r') as fobj:
        lst_lines = fobj.readlines()
    lines = list(map(lambda x: x[:-1], lst_lines[:-1])) # 去掉前n-1行末尾的'\n'
    lines.append(lst_lines[-1])
    str_lines = ''.join(lines)

    with open(filename, 'w') as fobj:
        for i, char in enumerate(str_lines):
            fobj.write(char)
            if (i+1) % num == 0 and i > 0:
                fobj.write('\n')


reshape('out.txt', 8) # 设置每行不超过8
```


9–17. 文本处理. 
创建一个原始的文本文件编辑器. 你的程序应该是菜单驱动的, 有如下这些选项:
1) 创建文件(提示输入文件名和任意行的文本输入),
2) 显示文件(把文件的内容显示到屏幕),
3) 编辑文件(提示输入要修改的行, 然后让用户进行修改),
4) 保存文件, 以及
5) 退出.
```
# -*- coding: utf-8 -*-

content = []
filename = ''

def newfile():
    global content
    global filename
    filename = input('Please input a filename to be create: ')
    while True:
        try:
            line = input("Please input a row content: ")
            content.append(line + '\n')
        except (EOFError, KeyboardInterrupt):
            break


def editfile():
    dispalyfile()
    edit_row = int(input('Please input row number to edit: '))
    if edit_row > len(content) or edit_row < 0:
        print('You want edit row is not exist.') 
    else:
        new_row = input('Please input new row content: ')
    content[edit_row] = new_row + '\n'


def dispalyfile():
    for row, line in enumerate(content):
        print('[%s]\t%s' % (row, line), end='')

def savefile():
    with open(filename, 'w') as fobj:
        for line in content:
            fobj.write(line)


CMDs = {'n': newfile, 'd': dispalyfile, 'e': editfile, 's': savefile}


def showmenu():
    prompt = '''
    (N)ew
    (D)ispaly
    (E)dit
    (S)ave
    (Q)uit

    Enter your choice: '''

    while True:
        while True:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'

            print('\nYour picked: [%s]' % choice)

            if choice not in 'ndesq':  
                print('Invalid option, try again.')
            else:   # 正确的命令项，跳出输入命令循环
                break

        if choice == 'q':
            break       # 退出程序

        CMDs[choice]()

if __name__ == '__main__':
    showmenu()
```


9–18. 搜索文件. 提示输入一个字节值(0 - 255)和一个文件名. 显示该字符在文件中出现的次数.
```
def countbyte(filename, bytevalue):
    bytevalue = int(bytevalue)
    ch = chr(bytevalue)

    with open(filename, 'r', encoding='utf-8') as fobj:
        lines= fobj.readlines()
    content = ''.join(lines)
    count = 0
    for s in content:
        if s == ch:
            count += 1
    return count


print(countbyte('out.txt', '97')) # 97,即查找'a'的个数
```
count()函数。
```
def countbyte(filename, value):  
    ch = chr(value)  
    with open(filename, 'r') as f:  
        total = sum(item.count(ch) for item in f)  
    return total  

print(countbyte('out.txt', 97))
```

9–19. 创建文件. 
创建前一个问题的辅助程序. 创建一个随机字节的二进制数据文件, 但某一特定字节会在文件中出现指定的次数. 该程序接受三个参数:
1) 一个字节值( 0 - 255 ),
2) 该字符在数据文件中出现的次数, 以及
3) 数据文件的总字节长度.
你的工作就是生成这个文件, 把给定的字节随机散布在文件里, 并且要求保证给定字符在文件中只出现指定的次数, 文件应精确地达到要求的长度.
```
# -*- coding: utf-8 -*-

from random import randint

def countbyte(filename, value):  
    ch = chr(value)  
    with open(filename, 'r') as f:  
        total = sum(item.count(ch) for item in f)  
    return total  


def createrandomfile(total, bytevalue, num):
    '''
    文件全部的字符由其他字节值组成，然后在随机索引位置替换制定的字节值
    '''
    content_lst = list()
    i = 0
    while i < total:
        ch = chr(randint(0, 255))
        if ch == chr(bytevalue):
            continue
        else:
            content_lst.append(ch)
            i += 1

    for j in range(num):
        index = randint(0, total-1)
        content_lst[index] = chr(bytevalue)

    content_str = ''.join(content_lst)

    with open('out.txt', 'w') as fobj:
        fobj.write(content_str)


createrandomfile(800, 65, 1) # chr(65) = 'A'

print(countbyte('out.txt', 65)) # 验证出现的次数
```

9–20. 压缩文件. 
写一小段代码, 压缩/解压缩 gzip 或 bzip 格式的文件. 可以使用命令行下的 gzip 或 bzip2 以及 GUI 程序 PowerArchiver , StuffIt , 或 WinZip 来确认你的 Python支持这两个库.
```
import gzip  
  
def compress(zipfile, filename):  
    obj = gzip.open(zipfile, 'wb')  
    with open(filename, 'rb') as f:  
        obj.writelines(f)  
    obj.close()  
  
def decompress(zipfile, filename):  
    obj = gzip.open(zipfile, 'rb')  
    content = obj.read()  
    with open(filename, 'wb') as f:  
        f.write(content)  
  
if __name__ == '__main__':  
    compress('test.gzip', 'out.txt')  
    decompress('test.gzip', 'out1.txt') 
```

9–21. ZIP 归档文件. 
创建一个程序, 可以往 ZIP 归档文件加入文件, 或从中提取文件,有可能的话, 加入创建ZIP 归档文件的功能.
```
import zipfile  

def add_file(zipname, filename):  
    with zipfile.ZipFile(zipname, 'a') as obj:  
        obj.write(filename)  
  
def read_file(zipname, filename):  
    with zipfile.ZipFile(zipname, 'r') as obj:  
        content = obj.read(filename)
        print(content.decode('utf-8'))  

# out1.txt 和 out.txt 压缩到 test.zip 中  
add_file('test.gzip', 'out1.txt')  
add_file('test.gzip', 'out.txt')  

read_file('test.gzip', 'out1.txt')  
read_file('test.gzip', 'out.txt')  
```


9–22. ZIP 归档文件. 
unzip -l 命令显示出的 ZIP 归档文件很无趣. 创建一个 Python脚本 lszip.py , 使它可以显示额外信息: 压缩文件大小, 每个文件的压缩比率(通过比较压缩前后文件大小), 以及完成的 time.ctime() 时间戳, 而不是只有日期和 HH:MM .
提示: 归档文件的 date_time 属性并不完整, 无法提供给 time.mktime() 使用....这由你自己决定.


9–23. TAR 归档文件. 
为 TAR 归档文件建立类似上个问题的程序. 这两种文件的不同之处在于 ZIP 文件通常是压缩的, 而 TAR 文件不是, 只是在 gzip 和 bzip2 的支持下才能完成压缩工作. 加入任意一种压缩格式支持.附加题: 同时支持 gzip 和 bzip2 .


9–24. 归档文件转换. 
参考前两个问题的解决方案, 写一个程序, 在 ZIP (.zip) 和TAR/gzip (.tgz/.tar.gz) 或 TAR/bzip2 (.tbz/.tar.bz2) 归档文件间移动文件. 文件可能是已经存在的, 必要时请创建文件.


9–25. 通用解压程序.
创建一个程序, 接受任意数目的归档文件以及一个目标目录做为参数.归档文件格式可以是 .zip, .tgz, .tar.gz, .gz, .bz2, .tar.bz2, .tbz 中的一种或几种. 程序会把第一个归档文件解压后放入目标目录, 把其它归档文件解压后放入以对应文件名命名的目录下(不包括扩展名). 例如输入的文件名为 header.txt.gz 和 data.tgz ， 目录为 incoming ,header.txt 会被解压到 incoming 而 data.tgz 中的文件会被放入 incoming/data .


