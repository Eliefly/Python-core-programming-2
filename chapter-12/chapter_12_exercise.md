# 第12章 模块和文件

标签（空格分隔）： python-core-2

---

12-1 路径搜索和搜索路径。路径搜索和搜索路径之间有什么不同？
```
路径搜索是指在文件系统“预定义区域”中查查找特定的文件。这些“预定义区域”就是你python搜索路径的集合。
所以，路径搜索是指查找某个文件的操作，强调搜索这个过程。搜索路径是要去查找的一组目录。
```

12-2 导入属性。假设你的模块 mymodule 里有一个 foo() 函数。
(a)把这个函数导入到你的名称空间有哪两种方法？
(b)这两种方法导入后的名称空间有什么不同？
```
from mymodule import foo
从mymodule中的foo导入当前名称空间，可以直接用foo访问。
import mymodule
导入mymodule整个模块到当前名称空间，需要是用 mydule.foo 访问。
```

12-3 导入“import module” 和“from module import *” 有什么不同？
```
import module, module内的对象还在 module空间下，访问单个的对象var需要 module.var。
from module import *， module内的所有对象直接导入了当前名称空间，可以直接访问使用。
```

12-4 名称空间和变量作用域有什么不同？
```
名称空间是纯粹意义上的名字和对象间的映射关系，强调是否存在。而作用域还指出了从用户的哪些物理位置可以访问到这些对象。
```

12–5 使用 __import__().
(a) 使用 __import__ 把一个模块导入到你的名称空间。 你最后使用了什么样的语法?
(b) 和上边相同, 使用 __import__() 从指定模块导入特定的名字。

```
time = __import__('time')
print(time.ctime())

# 加上fromlist参数好像也没直接实现from time import ctime的效果
time = __import__('time', globals(), locals(), fromlist=['ctime'])
ctime = time.ctime
print(ctime())
```
12–6 扩展导入。
创建一个 importAs() 函数. 这个函数可以把一个模块导入到你的名称空间, 但使用你指定的名字, 而不是原始名字。 例如, 调用 newname=importAs('mymodule') 会导入mymodule , 但模块和它的所有元素都通过新名称 newname 或 newname.attr 访问。 这是 Python2.0 引入的扩展导入实现的功能。
```
def importAS(modulename):
    newmodule = __import__(modulename)
    return newmodule

newmodule = importAS('time')
print(newmodule.ctime())
```
12–7 导入钩子。
研究 PEP 302 的导入钩子机制. 实现你自己的导入机制, 允许编码你的模块(encryption, bzip2, rot13, 等), 这样解释器会自动解码它们并正确导入。你可以参看 zip文件导入的实现 (参阅 第 12.5.7 节)。
```
看不大懂。导入编码/归档压缩(如zip, bzip2, rot13，base64)格式的模块？
http://blog.csdn.net/reimuko/article/details/28269219
```
