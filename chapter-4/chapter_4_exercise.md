# 第4章 Python对象

---
```
# -*- coding: utf-8 -*-
# !/usr/bin/python3.5
```

##### 4-1 Python 对象。与所有 Python 对象有关的三个属性是什么？请简单描述一下。
```
Python对象都拥有的3个特性：身份（内存地址），类型，值。
身份：每个对象都有一个唯一的身份标示自己，可以被认为是该对象的内存地址，可以使用内建函数 id() 来查看。
类型：对象的类型决定该对象可以保存什么类型的值，可以进行什么样的操作，以及遵循什么规则。可以使用内建函数 type() 查看对象类型。
值：对象存储的数据项。
```
##### 4-2 不可更改（immutable）指的是什么？Python 中哪些类型是不可更改的，哪些不是？
```
不可更改是是指：在不改变对象 id 的情况下，无法改变对象的值。（改变了对象 id 则其实就是新建对象取代旧对象，不是在原有对象上做更改）
可更改的对象有：列表，字典
不可更改的对象有：数字，字符串，元组

如下，改变数字对象 a 的值，可以看到对象的身份 id 已经改变了。两个 a 不是同一对象。
>>> a = 1
>>> id(a)
1647916816
>>> a = 2
>>> id(a)
1647916832
```

##### 4-3 哪些Python的类型是按照顺序访问的，它们和映射类型有什么不同？
```
字符串、列表、元组 是按照顺序访问的，可以按照从0开始的索引顺序访问，一次可以访问一个或多个元素，也即支持切片访问。
映射类型有类似的索引属性，不过它的索引并不使用顺序的数字偏移量取值，它的元素是无序存放的。通过一个唯一的键值来访问，这就是映射类型，它容纳的是哈希键-值对的集合。
```

##### 4-4 type()。内建函数 type() 做什么？type() 返回的对象是什么？
type(object) 返回对象object的类型。type() 返回的对象是 class 类型。
```
>>> type(1)
<class 'int'>
>>> type('123')
<class 'str'>
>>> type(1+2j)
<class 'complex'>
>>> class FOO():
...     pass
...
>>> foo = FOO()
>>> type(FOO)
<class 'type'>
>>> type(foo)
<class '__main__.FOO'>
```
##### 4-5 str() 和 repr()。内建函数str() 和 repr()之间的不同是什么？哪一个等价于反引号(``)操作符？
```
str() 从一个给定对象转化得到字符串对象。 
repr() 是将一个对象转成字符串显示，可以被Python解释器识别。
两者都是为了可读性更好的字符串表示。 repr() 输出对 Python比较友好，而str()的输出对用户比较友好。
对有些对象来说两者没有明显的区别，如数字，列表，字典。
>>> str(1.0)
'1.0'
>>> repr(1.0)
'1.0'
>>> eval(str(1.0))
1.0
>>> eval(repr(1.0))
1.0

>>> str([1, 2, 3])
'[1, 2, 3]'
>>> repr([1, 2, 3])
'[1, 2, 3]'
>>> eval(str([1, 2, 3]))
[1, 2, 3]
>>> eval(repr([1, 2, 3]))
[1, 2, 3]

repr() 转换的对象值 通常可以 使用 eval() 函数重新得到对象的值。
>>> s = 'abcd'
>>> str(s)
'abcd'
```

##### 4-6 对象相等。你认为 type(a) == type(b) 和 type(a) is type(b) 之间的不同是什么？为什么回选择后者？函数isinstance() 与这有什么关系？
```
函数 isinstance(object, classinfo) 返回布尔值，如果参数object是classinfo的实例，或者object是classinfo类的子类的一个实例， 
返回True。如果object不是一个给定类型的的对象， 则返回结果总是False。
>>> isinstance(1, int)
True
>>> isinstance(1.0, int)
False
>>> isinstance(1.0, (int, float))
True

能用type()判断的类型一般也可以用 isinstance() 判断，明显的区别在子类的判断上，isinstance() 会认为子类是一种父类类型。
>>> class FOO():
...     pass
...
>>> class BAR(FOO):
...     pass
...
>>>
>>> bar = BAR()
>>> isinstance(bar, FOO)
True
```
##### 4-7 内建函数 dir()。在第二章的几个练习中，我们用内建函数 dir()做了几个实验， 它接受一个对象，然后给出相应的属性。请对 types 模块做相同的实验。记下您熟悉的类型， 包括您对这些类型的认识，然后记下你还不熟悉的类型。在学习 Python 的过程中，你要逐步将 “不熟悉”的类型变得“熟悉”起来。
```
>>> dir(type)
['__abstractmethods__', '__base__', '__bases__', '__basicsize__', '__call__', '_
_class__', '__delattr__', '__dict__', '__dictoffset__', '__dir__', '__doc__', '_
_eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__gt__', '__ha
sh__', '__init__', '__instancecheck__', '__itemsize__', '__le__', '__lt__', '__m
odule__', '__mro__', '__name__', '__ne__', '__new__', '__prepare__', '__qualname
__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__
str__', '__subclasscheck__', '__subclasses__', '__subclasshook__', '__text_signa
ture__', '__weakrefoffset__', 'mro']
```

##### 4-8 元组和列表。相同点是什么？不同点是什么？
```
相同点：都是容器存储类型，可容纳多个对象。都是顺序访问，可以从0开始的索引顺序访问。
不同点：列表是可更改类型，元组是不可更改类型。
```
##### 4-9 实践，给定以下赋值：
```
a = 10
b = 10
c = 100
d = 100
e = 10.0
f = 10.0
```
请问下面各表达式的输出是什么？为什么？
```
(a) a is b
(b) c is d
(c) e is f
```
```
a和b，c和d指向同一对象。e和f指向不同的对象。
Python 回缓存简单的类型（小整形，范围是（-1, 100）,但这个范围是会变的)，造成我们认为应该新建对象时，它却没有新建对象的假象。
>>> a = 10
>>> b = 10
>>> c = 100
>>> d = 100
>>> e = 10.0
>>> f = 10.0
>>>
>>> a is b
True
>>> c is d
True
>>> e is f
False
```
