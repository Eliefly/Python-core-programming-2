# 第14章 执行环境

标签（空格分隔）： python-core-2

---

## 14-1. 可调用对象。说出Python中的可调用对象。exec语句和内建函数eval()有什么不同？
```
python可调用的对象有：
1.函数：内建函数(Built-in Functions)，如abs(),dict(),help()等；用户自定义函数，包括def关键字和lambda定义的；
>>> type(isinstance)
<class 'builtin_function_or_method'>

2.方法：内建方法(methods of built-in classes)，如sys.exit()；用户自定义方法，即自定义内的方法；
>>> type(list.append)
<class 'method_descriptor'>

3.类，创建实例就是调用类

4.实现了__call__方法的类实例
class Myclass():
    def __call__(self, *args):
        print('invoke instance')

ins = Myclass()
print(callable(ins))
# True
```
```
eval()可以执行字符串形式的表达式，或经过compile编译的代码对象（编译选项'eval'）。
>>> eval('1+1')
2
>>> eval('a = 1+1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1
    a = 1+1
      ^
SyntaxError: invalid syntax

exec()可以执行字符串形式的python代码(执行字符串表达式返回None)，或经过compole编译的代码对象（编译选项'exec）。
>>> exec('1 + 1')
>>> exec('a = 1 + 1')
>>> a
2
```
## 14-2. input()和raw_input()。
内建函数 input()和 raw_input() 有什么不同。
```
python2中，input()输入的内容会转化字符串，raw_input()等价于eval(input())。
python3中raw_input()转化为input()，没有raw_input()了。
```

## 14-3.执行环境。
创建运行其他Python脚本的脚本。
```
在python2中，execfile(filename)即可。
python3中execfile()被移除了， execfile() 相当于封装执行open(), compile(), 和 exec()

with open('test.py', 'r') as fobj:
    lines = fobj.readlines()
        lines = ''.join()
    codeobj = compile(lines, '', 'exec')
    exec(codeobj)
```

## 14-4. os.system()。
选择你熟悉的系统命令，该命令执行任务市不需要输入，也不输出到屏幕或根本不输出任何东西。调用os.system()运行程序。附加题：将你的解决方案移植到subprocess.call()。
```
# windows下
import os 
os.system('calc.exe')

import subprocess
subprocess.call('calc.exe')
```

## 14-5. commands.getoutput()。
用commands.getoutput()解决前面的问题。
```
python3:No module named 'commands'
```

## 14-6.popen()家族。
选择熟悉的系统命令，该命令从标准输入获得文本，操作或输出数据。使用os.popen()与程序进行通信。输出到哪儿？使用 popen2.popen2()代替。
啥意思？
```
 If the cmd argument to popen2 functions is a string, the command is executed through /bin/sh. If it is a list, the command is directly executed.
 
(child_stdout, child_stdin) = popen2.popen2("somestring", bufsize, mode)
==>
p = Popen("somestring", shell=True, bufsize=bufsize,
          stdin=PIPE, stdout=PIPE, close_fds=True)
(child_stdout, child_stdin) = (p.stdout, p.stdin)

(child_stdout, child_stdin) = popen2.popen2(["mycmd", "myarg"], bufsize, mode)
==>
p = Popen(["mycmd", "myarg"], bufsize=bufsize,
          stdin=PIPE, stdout=PIPE, close_fds=True)
(child_stdout, child_stdin) = (p.stdout, p.stdin)
```
## 14-7.subprocess模块。
把先前问题的解决方案移植到subprocess模块。

## 14-8.exit函数。
设计一个在程序退出时的函数，安装到sys.exitfunc()，运行程序，演示你的exit函数确实被调用了。
```
# Changes assignment of sys.exitfunc to use of the atexit module.
import sys  
import atexit
  
def foo():  
    print('show message')  

atexit.register(foo)  
print('123')  
# 123
# show message
```

## 14-9.Shells.
创建shell(操作系统接口)程序。给出接受操作系统命令的命令行接口（任意平台）。



## 14-10. fork()/exec*()和spawn*()的比较。
使用fork()-exec*()对和spawn*()家族函数有什么不同？哪一组功能更强？

## 14-11生成和执行python代码。
用funcAttrs.py脚本（例14.4）加入测试代码到已有程序的函数中。创建一个测试框架，每次遇到你特殊函数属性，它都会运行你的测试代码。
