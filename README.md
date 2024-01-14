# 文件夹说明
--myDjango     #Django框架学习
--learnRpa     #RPA自动办公
--learnCrawler #爬虫
--leetCode     #leetCode     
--utils        #公共类，配置等

### Python基础知识 ###
# Python3 简介
Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。
Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。
Python 是一种解释型语言： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
Python 是交互式语言： 这意味着，您可以在一个 Python 提示符 >>> 后直接执行代码。
Python 是面向对象语言: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。
Python 是初学者的语言：Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

# Python 发展历史
Python 是由 Guido van Rossum 在八十年代末和九十年代初，在荷兰国家数学和计算机科学研究所设计出来的。
Python 本身也是由诸多其他语言发展而来的,这包括 ABC、Modula-3、C、C++、Algol-68、SmallTalk、Unix shell 和其他的脚本语言等等。
像 Perl 语言一样，Python 源代码同样遵循 GPL(GNU General Public License)协议。
现在 Python 是由一个核心开发团队在维护，Guido van Rossum 仍然占据着至关重要的作用，指导其进展。
Python 2.0 于 2000 年 10 月 16 日发布，增加了实现完整的垃圾回收，并且支持 Unicode。
Python 3.0 于 2008 年 12 月 3 日发布，此版不完全兼容之前的 Python 源代码。不过，很多新特性后来也被移植到旧的Python 2.6/2.7版本。
Python 3.0 版本，常被称为 Python 3000，或简称 Py3k。相对于 Python 的早期版本，这是一个较大的升级。
Python 2.7 被确定为最后一个 Python 2.x 版本，它除了支持 Python 2.x 语法外，还支持部分 Python 3.1 语法。

# 保留字符
and	assert break class continue
def del elif else except exec 
finally for from global if import
in is lambda not or pass print
raise return try while with yield

# 运算符
算术运算符：+，-，*，/，%，**，//
比较运算符：==，!=，<>，>，<，>=，<=
赋值运算符：=，+=，-=，*=，/=，%=，**=，//= 
位运算符：&，|，^，~，<<，>>
逻辑运算符：and，or，not
成员运算符：in，not in
身份运算符：is，is no

# 命名规范
模块名写法: module_name
包名写法: package_name
类名: ClassName
方法名: method_name
异常名: ExceptionName
函数名: function_name
全局常量名: GLOBAL_CONSTANT_NAME
全局变量名: global_var_name
实例名: instance_var_name
函数参数名: function_parameter_name
局部变量名: local_var_name

# 七个标准数据类型
数字（Numbers）：int,float,complex;i=1,f=1.1,c=a+bj
布尔（Boolean）：True,False;b=False
字符串（String）：单引号,双引号;str='abc'
列表[ ]（list）：有序可改变集合,允许重复数据;list=[1,2,3,4]
元组( )（tuple）：有序不可改变集合,允许重复数据;tup=(1,2,3,4)
集合{ }（set）：无序无索引（索引为键值）集合,无重复数据;s={'a',"b",1,(1,2),"abc"},s=set();
              由一个或数个形态各异的大小整体组成,创建一个空集合必须用set()而不是{ },不能往集合里边添加可变数据类型的数据
字典{ }（dictionary）：无序,可变,有索引集合,无重复数据;dic={'a':12,'b':34}

# 类成员可见性
public：xx
protected：_xx
private:__xx
特列方法: __xx__

# 系统变量--在程序运行时自动创建的变量，这些变量的命名与程序本身的变量命名不同，它们也不需要被程序员显式地进行声明
1. __name__
__name__是Python中的一个系统变量，它用于判断当前模块是被导入还是直接运行的。如果当前模块是被导入的，则__name__的值为模块名（即文件名），否则__name__的值为'__main__'。
2. __file__
__file__是Python中的另一个系统变量，它用于表示当前文件的路径。如果当前文件是被导入的，则__file__的值为被导入文件的路径，否则__file__的值为当前文件的路径。
3. __doc__
__doc__是Python中的文档字符串（Docstring），它用于描述模块、函数、类等对象的用途。文档字符串可以通过help()函数进行查看。
4. __annotations__
__annotations__是Python中的另一个系统变量，它用于存储变量、函数或类等对象的注解信息。注解信息可以为对象提供额外的元数据。
5. __builtins__
__builtins__是Python中的内置模块，它包含了Python中内置的函数、类、变量等内容。内置函数可以在任何Python程序中直接调用，无需进行导入。
6. __package__
__package__是Python中的一个系统变量，它用于表示当前模块所在的包。如果当前模块不在任何包中，则__package__的值为None。
7. __loader__
__loader__是Python中的另一个系统变量，它用于表示当前模块的加载器。加载器负责加载模块，处理模块的依赖关系等。
8. __spec__
__spec__是Python中的另一个系统变量，它用于表示当前模块的规范。规范描述了模块在导入时的行为、依赖关系等信息。
9. __cached__
__cached__是Python中的一个系统变量，它用于表示当前模块的缓存路径。如果当前模块在缓存中，则__cached__的值为缓存路径，否则__cached__的值为None。

#
python程序是从上而下逐行运行的，在.py文件中，除了def后定义函数外的代码都会被认为是“main”方法中的内容从上而下执行。
python没有main()方法。所谓的入口其实也就是个if条件语句，判断成功就执行一些代码，失败就跳过。没有java等其余语言中那样会有特定的内置函数去识别main()方法入口，在main()方法中从上而下执行
if __name__ == "__main__"的使用场景：测试过程中，为了保证代码正常运行，且这个代码需要被导入到另外一个脚本时，在这种情况下，我们通常不希望该脚本作为主模块运行。这样，就可以在导入和命令行测试情况下会有不同的执行和结果。创建一个库，但希望为用户做一个演示或其他特殊的运行时情况。通过使用这个 if 语句，使用你的代码作为库的 Python 模块就不会受到影响

# 继承的基本语法
class ClassName(baseclass-list):#ClassName:用于指定类名;baseclass-list:用于指定要继承的基类，多个用逗号“,”隔开,如不指定,将使用所有根类object
	statement			        #类体

## Python内置函数
# abs()
--abs(x)--返回数字的绝对值。
# all()
--all(iterable):--用于判断给定的可迭代参数iterable中的所有元素是否都为TRUE，如果是返回True，否则返回False。元素除了是0、空、None、False外都算True。
# any()	
--any(iterable)--用于判断给定的可迭代参数iterable是否全部为False，则返回False，如果有一个为True，则返回True。元素除了是0、空、FALSE外都算TRUE。
# ascii()
--ascii(object)--类似repr()函数, 返回一个表示对象的字符串, 但是对于字符串中的非ASCII字符则返回通过repr()函数使用\x,\u或\U 编码的字符。
# bin()	
--bin(x)--返回一个整数int或者长整数long int的二进制表示。
# bool()
--bool([x])--用于将给定参数转换为布尔类型，如果没有参数，返回False。
# bytearray()
--bytearray([source[, encoding[, errors]]])--返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0<=x<256。
# bytes()
--bytes([source[, encoding[, errors]]])--返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本。
# callable()
--callable(object)--可调用返回 True，否则返回False。
# chr()	
--chr(i)--返回值是当前整数对应的ASCII字符。
# classmethod()	
--修饰符对应的函数不需要实例化，不需要self参数，但第一个参数需要是表示自身类的cls参数，可以来调用类的属性，类的方法，实例化对象等。
# compile()	
--compile(source, filename, mode[, flags[, dont_inherit]])--将一个字符串编译为字节代码。
# complex()	
--complex([real[, imag]])--用于创建一个值为real+imag*j的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
# delattr()
--delattr(object, name)--用于删除属性。
# dict()
--dict(**kwarg)--dict(mapping, **kwarg)--dict(iterable, **kwarg)--用于创建一个字典。
>>>numbers1 = dict([('x', 5), ('y', -5)]) # 没有设置关键字参数，numbers1 = {'y': -5, 'x': 5}
>>>numbers2 = dict([('x', 5), ('y', -5)], z=8) # 设置关键字参数，numbers2 = {'z': 8, 'y': -5, 'x': 5}
>>>numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3]))) # zip()创建可迭代对象，numbers3 = {'z': 3, 'y': 2, 'x': 1}
# dir()	
--dir([object])--返回模块的属性列表。
# divmod()
--divmod(a, b)--接收两个数字类型（非复数）参数，返回一个包含商和余数的元组(a//b,a%b)。
# enumerate()
--enumerate(sequence, [start=0])--用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标。
--for index,num in enumerate(nums):
# eval()
--eval(expression[, globals[, locals]])--用来执行一个字符串表达式，并返回表达式的值。--eval( '3 * x' )--eval('pow(2,2)')
# exec()
--exec(object[, globals[, locals]])--执行储存在字符串或文件中的Python语句
# filter()
--filter(function, iterable)--用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象。--newlist = filter(n % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# float()
--float([x])--用于将整数和字符串转换成浮点数。
# format()
--格式化字符串的函数str.format()
>>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序，'hello world'
>>>"{1} {0} {1}".format("hello", "world")  # 设置指定位置，'world hello world'
>>>print("myname:{name}, myaddr:{addr}".format(name="hello", addr="world")) # myname:hello, myaddr:world
# frozenset()
--frozenset([iterable])--返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
# getattr()
--getattr(object, name[, default]) #object对象；name字符串，对象属性；default默认返回值，如果不提供该参数，在没有对应属性时，将触发AttributeError。--返回一个对象属性值。
# globals()
--以字典类型返回当前位置的全部全局变量。
# hasattr()
--hasattr(object, name)--判断对象是否包含对应的属性。
# hash()
--hash(object)--获取取一个对象（字符串或者数值等）的哈希值。
# help()
--help([object])--用于查看函数或模块用途的详细说明。
# hex()
--hex(x)--用于将一个指定数字转换为16进制数。
# id()
--id([object])--返回对象的唯一标识符，标识符是一个整数。
# input()
--input([prompt])--接受一个标准输入数据，返回为string类型。
# int()
--int(x, base=10) #x字符串或数字。base进制数，默认十进制。--将一个字符串或数字转换为整型。
# isinstance()
--isinstance(object, classinfo)--判断一个对象是否是一个已知的类型，类似type()。
# issubclass()
--issubclass(class, classinfo)--判断参数class是否是类型参数classinfo的子类。
# iter()
--iter(object[, sentinel])--用来生成迭代器。
# len()
--len( s )--返回对象（字符、列表、元组等）长度或项目个数。
# list()
--list( seq )--将元组或字符串转换为列表。
# locals()
--以字典类型返回当前位置的全部局部变量。
# map()
--map(function, iterable, ...)--根据提供的函数对指定序列做映射。
# max()
--max( x, y, z, .... )--返回给定参数的最大值，参数可以为序列。
# memoryview()
--memoryview(obj)--返回给定参数的内存查看对象(memory view)。
# min()
--min( x, y, z, .... )--返回给定参数的最小值，参数可以为序列。
# next()
--next(iterable[, default])--返回迭代器的下一个项目。
# object()
--object()--返回一个空对象，我们不能向该对象添加新的属性或方法。
# oct()
--oct(x)--一个整数转换成8进制字符串，8进制以0o作为前缀表示。
# open()
--open(file, mode='r')--用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出OSError。
# ord()
--ord(c)--是chr()函数（对于8位的ASCII字符串）的配对函数，它以一个字符串（Unicode字符）作为参数，返回对应的ASCII数值，或者Unicode数值。
# pow()
--pow(x, y[, z])--计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y)%z
# print()
--用于打印输出
# property()
--property([fget[, fset[, fdel[, doc]]]]) #fget获取属性值的函数；fset设置属性值的函数；fdel删除属性值函数；doc 属性描述信息。--在新式类中返回属性值。
# range()
--range(stop)--range(start, stop[, step]) #创建一个整数列表; #start起始值，默认0;stop结束值，但不包括stop;step步长，默认为1，不可以为0。--range(1,3):从1到3，不包含3，即1,2
# reload()
--reload(module)--用于重新载入之前载入的模块。
# repr()
--repr(object)--将对象转化为供解释器读取的形式。
# reversed()
--reversed(seq)--返回一个反转的迭代器。
# round()
--round( x [, n]  ) #x数值表达式；n数值表达式，表示从小数点位数。--返回浮点数x的四舍五入值。
# set()
--set([iterable])--创建一个无序不重复元素集
# setattr()
--setattr(object, name, value)--用于设置属性值，该属性不一定是存在的。如果属性不存在会创建一个新的对象属性，并对属性赋值
# slice()
-- slice(stop)--slice(start, stop[, step])--实现切片对象，主要用在切片操作函数里的参数传递。
# sorted()
--sorted(iterable, key=None, reverse=False)--对所有可迭代的对象进行排序操作。
# staticmethod()
--返回函数的静态方法--静态方法无需实例化，也可以实例化后调用
# str()
--str(object='')--将对象转化为适于人阅读的形式。
# sum()
--sum(iterable[, start]) #iterable可迭代对象，如：列表、元组、集合；start指定相加的参数，如果没有设置这个值，默认为0。--对序列进行求和计算。
# super()
--super(type[, object-or-type])--用于调用父类(超类)的一个方法。
# tuple()
--tuple( iterable )--将可迭代系列（如列表）转换为元组。
# type()
--type(object)--type(name, bases, dict) #name类的名称；bases基类的元组；dict字典，类内定义的命名空间变量。--如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
--isinstance()与type()区别：type()不会认为子类是一种父类类型，不考虑继承关系。isinstance()会认为子类是一种父类类型，考虑继承关系。如果要判断两个类型是否相同推荐使用isinstance()。
# vars()
--vars([object])--返回对象object的属性和属性值的字典对象。
# zip()
--zip([iterable, ...])--用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象。
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b) # 返回一个对象
>>> list(zipped)  # list()转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> list(zip(a,c)) # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> a1, a2 = zip(*zip(a,b)) # 与zip相反，zip(*)可理解为解压，返回二维矩阵式
>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]
# __import__()
--__import__(name[, globals[, locals[, fromlist[, level]]]]) #name模块名--用于动态加载类和函数。

## 其它
# 切片
object[start_index : end_index : step] #切片(slice)是对序列型对象(如list, string, tuple)的一种高级索引方法
>>> a = [1,2,[1,2]]
>>> b = a #赋值，指向的同一个内存地址
>>> c = a[:] #浅拷贝，二者是独立的对象，但他们的子对象还是指向统一对象（是引用）
>>> d = copy.copy(a) #浅拷贝，二者是独立的对象，但他们的子对象还是指向统一对象（是引用）
>>> e = copy.deepcopy(a) #深拷贝，是一个新的实体对象

# 垃圾回收
--引用计数：是Python的主要垃圾收集技术。每当Python对象被引用时，例如通过赋值操作，其引用计数就会增加。当对象的引用被删除或对象的作用域被销毁时，其引用计数就会减少。当引用计数达到0时，Python的垃圾收集器就会释放这块内存。
--周期性垃圾收集器：它的工作原理比较复杂，但简单来说，它会定期检查所有的对象，找出那些循环引用的对象，然后删除它们，即使它们的引用计数不为0。这样，Python就能回收循环引用的对象，防止内存泄漏。
