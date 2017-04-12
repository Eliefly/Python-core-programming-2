# 第13章 面向对象编程 

标签（空格分隔）： python-core-2

---
```
class Myclass(object):
    pass

obj = Myclass()

print('*'*20)
# 继承关系：Myclass --> object --> None
print(Myclass.__base__)     # <class 'object'>
print(object.__base__)      # None
print(type.__base__)        # <class 'object'>


print('*'*20)
print(obj.__class__)        # <class '__main__.Myclass'>
# Myclass, object, type 都是 type 类型
print(Myclass.__class__)    # <class 'type'>
print(type.__class__)       # <class 'type'>
print(object.__class__)     # <class 'type'>


print('*'*20)
print(isinstance(obj, type))        # False
print(isinstance(obj, object))      # True

# type 即使实例对象又是类对象?
print(isinstance(type, object))     # True
print(issubclass(type, object))     # True
```
从标准`float`派生`RoundFloat`:
```
class RoundFloat(float):
    def __new__(self, val):
        return super(RoundFloat, self).__new__(self, round(val, 2))

ret = RoundFloat(5.334)
print(ret)
# 5.33
```
定制`RoundFloat`:
```
class RoundFloat():
    def __init__(self, val):
        assert isinstance(val, float) or isinstance(val, int),\
             'Value must be a num.'
        self.value = round(val, 2)

    def __str__(self):
        return '%.2f' % self.value

    __repr__ = __str__


ret = RoundFloat(4.1)
print(ret)
ret = RoundFloat(3)
print(ret)
```
**包装**（用处不大）
```
from time import time, ctime

class TimedWrapMe(object):

    def __init__(self, obj):
        self.__data = obj
        self.__ctime = self.__atime = self.__mtime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def gettimeval(self, t_type):
        if not isinstance(t_type, str) or \
                t_type[0] not in 'cam':
            raise TypeError("argument of 'c', 'm', or 'a' req'd")
        return getattr(self, '_%s__%stime' % (self.__class__.__name__, t_type[0]))

    def gettimestr(self, t_type):
        return ctime(self.gettimeval(t_type))

    def set(self, obj):
        self.__data = obj
        self.__ctime = self.__atime = time()

    def __str__(self):
        self.__atime = time()
        return(str(self.__data))

    __repr__ = __str__


    def __getattr__(self, attr):
        self.__atime = time()
        return(getattr(self.__data, attr))


timeWrappedObj = TimedWrapMe(932)
print(timeWrappedObj.gettimestr('c'))
print(timeWrappedObj.gettimestr('m'))
print(timeWrappedObj.gettimestr('a'))

print(timeWrappedObj)
print(repr(timeWrappedObj))

timeWrappedObj.set('time is up!')
print(timeWrappedObj)
```


```

import os
import pickle

class FileDescr(object):
    saved = []

    def __init__(self, name=None):
        self.name = name

    def __get__(self, obj, type=None):
        if self.name not in FileDescr.saved:
            raise AttributeError('%r used before assignment' % self.name)

        try:
            f = open(self.name, 'r')
            val = pickle.load(f)
            f.close()
            return val
        except (pickle.UnpicklingError, IOError, EOFError, AttributeError,
                ImportError, IndexError) as e:
            raise AttributeError('could not read %r: %s' % (self.name, e))

    def __set__(self, obj, val):
        f = open(self.name, 'w')
        try:
            try:
                pickle.dump(val, f)
                FileDescr.saved.append(self.name)
            except (TypeError, pickle.PicklingError) as e:
                raise AttributeError('could not pickle %r: %s' % (self.name, e))

        finally:
            f.close()

    def __delete__(self, obj):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except (OSError, ValueError) as e:
            pass
```


----------

## 13-2. 函数和方法之间的区别是什么？
```
是否绑定在对象上，类中定义的函数过程就是类的方法。
```

## 13-3.对类进行定制。
写一个类，用来将浮点型值转换为金额。
```
class MoneyFmt(object):
    def __init__(self, data):
        self._data = data

    def update(self, data):
        self._data = data

    def dollarize(self):
        number = self._data
        if number < 0:
            number = abs(number)
        strnum = '%.2f' % number
        intger = strnum[:-3]
        intger = intger[::-1] # 字符串逆序
        lst = list(intger)
        # 适当位置插入','
        num = 0
        for i in range(1, len(lst)):
            if i % 3 == 0:
                lst.insert(i+num, ',')
                num += 1
        tmp = ''.join(lst)
        tmp = tmp[::-1]

        tmp = '$' + tmp + strnum[-3:]

        if self._data < 0:
            tmp = '-' + tmp
        return tmp

    # python3: __nonzero__() is now __bool__()
    def __bool__(self):
        return self._data > 0.5

    def __repr__(self):
        return str(self._data)

    def __str__(self):
        return self.dollarize()

ins = MoneyFmt(-12345.67)

ins.update(1234567.89)

print(repr(ins)) # __repr__

print(bool(ins)) # __bool__

print(str(ins))  # __str__
```

## 13-4.用户注册。
建立一个用户数据库类，来管理一个系统，该系统要求用户在登录后才能访问某些资源。这个数据库类对用户进行管理，并在实例化操作时加载之前保存的用户信息，提供访问函数来添加或更新数据库的信息。在数据修改后，数据库会在垃圾回收时将新信息保存到磁盘。
```
import shelve
import time


class UserDB(object):

    def __init__(self, dbname=None):
        self._dbname = dbname
        if dbname == None:
            self._dbname = 'shelvDB'
        self._db = shelve.open(self._dbname)

    def insertuser(self):
        username = input('Input name you register: ')
        if username in self._db:
            print('Your inputed name is existed.')
            return None
        passwd = input('Input password: ')
        user = {}
        user['name'] = username
        user['passed'] = passwd
        user['atime'] = time.time()
        self._db[username] = user

    def login(self):
        username = input('Input user you want to login: ')
        if username not in self._db:
            print('Your input user is not exist.')
            return None
        passwd = input('Input password: ')

        if passwd == self._db[username]['passwd']:
            self._db[username]['atime'] = time.time() # update time
            return True
        else:
            return False

    def removeuser(self):
        username = input('Input user you want to remvoe: ')
        if username not in self._db:
            print('Your input user is not exist.')
            return None
        self._db.pop(username)

    def update(self):
        self._db.close()
        self._db = shelve.open(self._dbname)

    def showall(self):
        for name in self._db:
            print(self._db[name])

    def __del__(self):
        self._db.close()

# ins = UserDB()
# ins.insertuser()
# ins.login()
# ins.removeuser()
# ins.update()
# ins.showall()
# del ins
```
## 13-5.几何。
创建一个由有序数值对(x,y)组成的Point类，代表某个点的X和Y坐标。
```
class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return str((self._x, self._y))

    __repr__ = __str__

p = Point(2, 3)
print(p)
```

## 13-6.几何。
创建一个直线类，除主要属性：一对坐标值外，它还具有长度和斜线属性。你需要覆盖__repr__()方法，使得代表那条直线的字符串表示形式是由一对元组构成的元组。
```
from math import sqrt

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str((self.x, self.y))

    __repr__ = __str__

class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return sqrt(pow(self.p1.x - self.p2.x, 2) + \
            pow(self.p1.y - self.p2.y, 2))

    def slope(self):  
        try:  
            k = float(self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)  
        except ZeroDivisionError:  
            k = None  
        return k  

    def __str__(self):
        return '(%s, %s)' % (self.p1, self.p2)


p1 = Point(1, 4)
p2 = Point(3, 5)
line = Line(p1, p2)

print(line.length())
print(line.slope())
print(str(line))
```

## 13-7.数据类。
提供一个time模块的接口，允许用户按照自己给定的时间格式来查看日期。你的类应该维护一个日期值，并用给定的时间创建一个实例，如果没有给出时间值，程序执行时会默认采用当前的系统时间。 
```
import time

class Mytime(object):
    def __init__(self, strtime=None):
        """strtime format: '1997-4-14'"""
        if strtime == None:
            struct_time = time.localtime()
        else:
            struct_time = time.strptime(strtime, '%Y-%m-%d')
        self.time = struct_time

    def update(self, strtime=None):
        if strtime == None:
            struct_time = time.localtime()
        else:
            struct_time = time.strptime(strtime, '%Y-%m-%d')
        self.time = struct_time       

    def display(self, mode):
        format_dict = {}
        format_dict['MDY'] = '%m/%d/%y'
        format_dict['MDYY'] = '%m/%d/%Y'
        format_dict['DMY'] = '%d/%m/%y'
        format_dict['DMYY'] = '%d/%m/%Y'
        format_dict['MODYY'] = '%m %d, %Y'

        if mode in format_dict:
            print(time.strftime(format_dict[mode], self.time))
        else:
            # 无效的格式输出：Mon Apr 14 00:00:00 1997 形式时间
            print(time.asctime(self.time))

ins = Mytime()
ins.update()
ins = Mytime('1997-4-14')
ins.display('MDY')
ins.display('MDYY')
ins.display('DMY')
ins.display('DMYY')
ins.display('MODYY')
ins.display('$$$$$')
```

## 13-8.堆栈类。
实现一个堆栈类，类中应该有push()和pop()方法，还有一个isempty()方法，如果堆栈是空的，返回布尔值1，否则返回0。一个交peek()方法，去除栈顶的数据，但不移除它。
```
# 借助list实现，后续学习数据结构，更深入点实现（Node数据节点）
class Stack(object):
    def __init__(self):
        self._data = list()

    def isempty(self):
        return len(self._data) == 0

    def push(self, ele):
        self._data.append(ele)

    def pop(self):
        if not self.isempty():
            return(self._data.pop())

    def peek(self):
        if not self.isempty():
            return(self._data[-1])

    def __repr__(self):
        return repr(self._data)

ins = Stack()
print(ins.isempty())
# True
ins.push(2)
ins.push(3)
ins.push(4)
print(ins)
# [2, 3, 4]
print(ins.pop())
# 4
print(ins)
# [2, 3]
print(ins.peek())
# 3
print(ins)
# [2, 3]
```
## 13-9.队列类。
实现一个队列类，这个类必须支持下面几种方法：enqueue()在队列的尾部加入一个新的元素，dequeue()在队列的头部取出一个元素，返回它并且把它从列表中删除。
```
class Queue(object):
    def __init__(self):
        self._data = list()

    def isempty(self):
        return len(self._data) == 0

    def enqueue(self, ele):
        self._data.append(ele)

    def dequeue(self):
        if not self.isempty():
            return(self._data.pop(0))

    def __repr__(self):
        return repr(self._data)

ins = Queue()
print(ins.isempty())
ins.enqueue(1)
ins.enqueue(2)
ins.enqueue(3)
print(ins)
# [1, 2, 3]
print(ins.dequeue())
# 1
print(ins)
# [2, 3]
```
## 13-10. 堆栈和队列
编写一个类，定义一个能够同时具有堆栈（FIFO）和队列（LIFO）操作行为的数据结构。
```
class StackQueue(object):
    def __init__(self):
        self._data = list()

    def isempty(self):
        return len(self._data) == 0

    # 在列表头“压入”一个新元素
    def unshift(self, ele):
        self._data = [ele] + self._data

    # 返回并删除第一个元素
    def shift(self):
        if not self.isempty():
            return(self._data.pop(0))

    # 在尾部加入一个新元素            
    def push(self, ele):
        self._data.append(ele)

    # 返回并删除最后一个元素
    def pop(self):
        if not self.isempty():
            return(self._data.pop())

    def __repr__(self):
        return repr(self._data)


ins = StackQueue()
ins.push(1)
ins.push(2)
ins.push(3)
print(ins)
ins.unshift(4)
ins.unshift(5)
print(ins)
print(ins.pop())
print(ins.shift())
```

## 13-11.电子商务。
你需要为一家B2C零售商编写一个基础的电子商务引擎。你需要写一个针对顾客的类User，一个对应存货清单的类Item，还有一个对应购物车的类叫Cart。货物放到购物车里，顾客可以有多个购物车。同时购物车里可以有多个货物，包括多个同样的货物。
```
class Item(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 更新价格
    def updateprice(self, price):
        self.price = price

    def __repr__(self):
        return ('(name:%s, price:%s)' % (self.name, self.price))

class Cart(object):
    def __init__(self):
        self.data = {}

    # 加入货物
    def add_goods(self, item, num=1):
        self.data[item] = num

    # 删除货物
    def remove_goods(self, item):
        if item in self.data:
            del self.data[item]

    # 清空购物车
    def clear_cart(self):
        self.data.clear()

    def __repr__(self):
        return str(self.data)

class User(object):
    def __init__(self, name):
        self.username = name
        self.cart = [Cart()]

    # 新增购物车
    def add_cart(self, cart=None):
        if isinstance(cart, Cart):
            self.cart.append(cart)
        elif cart == None:
            self.cart.append(Cart())

    # 删除购物车
    def del_cart(self, index):
        self.cart.pop(index)

    def __repr__(self):
        return ('%s: %s' % (self.username, self.cart))


apple = Item('apple', 6)
banana = Item('banana', 2)
soap = Item('soap', 4)
print(soap)

inscart = Cart()
inscart.add_goods(apple, 2)
inscart.add_goods(banana, 10)
print(inscart)
inscart.remove_goods(apple)
print(inscart)
inscart.add_goods(soap)
print(inscart)

user = User('jcak')
print(user)
user.add_cart(inscart)
print(user)
user.cart[0].add_goods(apple)
print(user)
user.del_cart(1)
print(user)
```

## 13-12.聊天室。
你需要三个类：一个Message类，它包含一个消息字符串以及诸如广播、单方收件人等其他信息。一个User类，包含了进入你聊天室的某个人的所有信息。一个Room类，它体现了一个更加复杂的聊天系统，用户可以在聊天时创建单独的房间，并邀请其他人加入。
```
# -*- coding: utf-8 -*-
class Message(object):
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

class User(object):
    def __init__(self, name):
        self.name = name
        self.user_room = []

    # 用户加入聊天室
    def joinRoom(self, room):
        self.user_room.append(room.name)
        room.room_user.append(self)

    # 用户发送msg
    def sendMsg(self, room, content, receiver='all'):
        # print('begin send msg...')
        if self in room.room_user:
            msg = Message(self, receiver, content)
            room.roomRec(msg)


    # 用户收msg
    def recMsg(self, message):
        print("'%s' receive from '%s'： '%s'" % \
            (message.receiver.name, message.sender.name, message.content))


    # 用户创建聊天室Room
    def createRoom(self, roomname):
        room = Room(roomname)
        self.joinRoom(room)
        return room

class Room(object):
    def __init__(self, name):
        self.name = name
        self.room_user = []

    # 聊天室添加用户
    def addUser(self, user):
        self.room_user.append(user)
        user.user_room.append(self.name)

    # 聊天室收到消息
    def roomRec(self, message):
        # 发送给特定user
        if message.receiver in self.room_user:
            message.receiver.recMsg(message)
        # 如果是群发
        elif message.receiver == 'all':
            for user in self.room_user:
                if user is not message.sender:
                    message.receiver = user # 依次修改接受者
                    user.recMsg(message)

if __name__ == '__main__':

    room = Room('room 1')

    jack = User('jack')
    andy = User('andy')
    michael = User('michael')

    room.addUser(jack)
    andy.joinRoom(room)
    michael.joinRoom(room)

    # 用户michael 创建room
    room2 = michael.createRoom('room 2')
    jack.joinRoom(room2)


    print(jack.user_room)
    print(andy.user_room)
    print(michael.user_room)
    # ['room 1', 'room 2']
    # ['room 1']
    # ['room 1', 'room 2']

    jack.sendMsg(room, 'message, jack to andy message', andy)
    # 'andy' receive from 'jack'： 'message, jack to andy message'
    andy.sendMsg(room, 'message, andy to all room user ')
    # 'jack' receive from 'andy'： 'message, andy to all room user '
    # 'michael' receive from 'andy'： 'message, andy to all room user '
    michael.sendMsg(room2, 'message, michael to all room2 user')
    # 'jack' receive from 'michael'： 'message, michael to all room2 user'
```
参考：http://blog.csdn.net/reimuko/article/details/28272057


## 13-14.DOS。
为DOS机器编写一个Unix操作界面的shell。你向用户提供一个命令行，使得用户可以在那里输入unix命令，你可以对这些命令进行解释，并把返回相应的输出。例如：“ls”命令调用“dir”来显示一个目录中的文件列表。
```
import os  
  
class Shell(object):  
  
    def __init__(self):  
        self.cmds = {'ls': 'dir', 'cat': 'type', 'rm': 'del'}  
  
    def translate(self, cmd):  
        words = cmd.split()  
        if words[0] in self.cmds:  # words[0]是命令，其他是参数
            words[0] = self.cmds[words[0]]  
        return ' '.join(words)  
  
    def start(self):  
        while True:  
            cmd = input('$')  
            cmd = self.translate(cmd)  
            if cmd == 'exit':  
                break  
            else:  
                os.system(cmd)  

if __name__ == '__main__':  
    sh = Shell()  
    sh.start()  
```

## 13-15 授权。
示例13.8的执行结果表明改写的CapOpen能成功的玩成数据的写入操作。我们在最后评论中，提到可以使用CapOpen() 或 open() 读取文件中的文本。为什么呢？这两者使用起来有什么不同？
```
class Capopen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return str(self.file)

    def write(self, line):
        self.file.write(line.upper())

    def __getattr__(self, attr):
        return getattr(self.file, attr)

# open()得到的文件对象是Capopen()实例的一个属性。write()通过f.write()调用，其他没有改写的如close()则要f.file.close()
f = Capopen('test.txt', 'w+')
f.write('this is test\n')
f.write('this is test\n')
f.file.close()

f = Capopen('test.txt', 'w+')
for eachline in f.file:
    print(eachline, end='')
```

## 13-16.授权和函数编程。
(a)请为示例中的CanOpen类编写一个writelines()方法，这个新函数可以一次读入多行文本，然后将文本转化为大写的形式。
(b)在writelines()方法中添加一个参数，用这个参数来指明是否需要为每行文本加上一个换行符。此参数的默认值是False，表示不加换行符。
```
import os
class Capopen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return str(self.file)

    def write(self, line):
        self.file.write(line.upper())

    def __getattr__(self, attr):
        return getattr(self.file, attr)

    def writelines(self, lines, flag=False):  
        for line in lines:
            if flag == True:
                line = line + os.linesep  
            self.write(line)


f = Capopen('test.txt', 'w+')
f.writelines(['line 1', 'line 2', 'line 3'])
```
## 13-17 数值类型子类化。
修改示例13.11中看到的moneyfmt.py,使它可以扩展Python的浮点类型。请确保它支持所有的操作，而且是不可变的。
```
# 和练习13-3实现基本一样
class MoneyFmt(object):
    def __init__(self, value=0.0):
        self.value = float(value)

    def update(self, value=None):
        self.value = float(value)
        return str(self.value)

    def dollarize(self):
        number = self.value
        if number < 0:
            number = abs(number)
        strnum = '%.2f' % number
        intger = strnum[:-3]
        intger = intger[::-1] # 字符串逆序
        lst = list(intger)
        # 适当位置插入','
        num = 0
        for i in range(1, len(lst)):
            if i % 3 == 0:
                lst.insert(i+num, ',')
                num += 1
        tmp = ''.join(lst)
        tmp = tmp[::-1]
        tmp = '$' + tmp + strnum[-3:]
        if self.value < 0:
            tmp = '-' + tmp
        return tmp

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return self.dollarize()

    def __bool__(self):
        return abs(self.value) > 0.5


cash = MoneyFmt(123.45)
print(bool(cash))
print(cash)
print(cash.update(100000.4567))
print(cash)
print(cash.update(-0.3))
print(cash)
print(repr(cash))
print(str(cash))
print(bool(cash))
```

## 13-19 字典子类。
若将keys()方法重写为：
```
class SortedKeyDict(dict):
    def keys(self):
        return sorted(self.keys())
```
调用keys()结果如何？如何解决？

```
# 会出现无线递归的调用。通过实例调用keys()方法，其中的sorted(self.keys())中再次通过实例调用了keys()。
class SortedKeyDict(dict):
    def keys(self):
        return sorted(super(SortedKeyDict, self).keys())


class SortedKeyDict(dict):
    def keys(self):
        return sorted(dict.keys(self))
```

## 13-20.类的定制。改进脚本time60.py
(a)允许“空”实例化：如果小时和分钟的值没有给出，默认为0小时0分钟。
(b)用0占位组成两位数的形式，因为当前的时间格式不符合要求。
(c)除了用hours(hr)和minutes(min)进行初始化外，还支持以下时间输入格式：
一个由小时和分钟组成的元组，如(10,30)
一个由小时和分钟组成的字典，如{'hr':10, 'min':30}
一个代表小时和分钟的字符串，如"10:30"
(e)实现__repr__()。
(f)添加60进制的运算功能。
```
class Time60(object):
    # def __init__(self, hr=0, min=0):
    #     self.hr = hr
    #     self.min = min

    def __init__(self, hr=None, min=None):
        # print(hr, min)
        if hr == None and min == None:
            self.hr = 0
            self.min = 0
        elif hr is not None and min is not None:
            self.hr = hr
            self.min = min
        elif hr is not None and isinstance(hr, tuple):
            self.hr = hr[0]
            self.min = hr[1]
        elif hr is not None and isinstance(hr, dict):
            self.hr = hr['hr']
            self.min = hr['min']
        elif hr is not None and isinstance(hr, str):
            tmp = hr.split(':')
            self.hr = int(tmp[0])
            self.min = int(tmp[1])
        self.update()

    def update(self):
        h, m = divmod(self.min, 60)
        self.hr = self.hr + h
        self.min = m        

    def __str__(self):
        return '%02d:%02d' % (self.hr, self.min)

    # __repr__ = __str__
    def __repr__(self):
        return "%s('%02d:%02d')" % (self.__class__.__name__, self.hr, self.min)

    def __add__(self, other):
        return self.__init__(self.hr + other.hr, self.min + other.min)

    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        self.update()
        return self

if __name__ == '__main__':
    ins1 = Time60((6, 100))
    print(ins1)
    ins2 = Time60({'hr':10, 'min':30})
    print(ins2)
    ins3 = Time60()
    print(ins3)
    ins4 = Time60('12:300')
    print(ins4)

    ins5 = Time60(3, 4)
    print(ins5)

    ins1 += ins2
    print(ins1)

    ins6 = Time60(4, 80)
    a = repr(ins6)
    b = eval(a)
    print(type(b))
    print(b)
```
