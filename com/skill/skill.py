#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import division
import ast
import copy

################1.枚举 - enumerate可以有参数哦  之前我们这样操作：

i = 0
for item in range(10):
    print(i, item)
    i += 1

# 现在我们这样操作：

for i, item in enumerate(range(10)):
    print(i, item)

# enumerate函数还可以接收第二个参数。就像下面这样：

list(enumerate('abc'))
# [(0, 'a'), (1, 'b'), (2, 'c')]

list(enumerate('abc', 1))
[(1, 'a'), (2, 'b'), (3, 'c')]

################2.字典 / 集合  解析  你也许知道如何进行列表解析，但是可能不知道字典 / 集合解析。它们简单易用且高效。就像下面这个例子：


# range()和xrange()在Python2里是两种不同的实现。但是在Python3里，range()这种实现被移除了；

# my_dict = {i: i * i for i in xrange(100)}
# my_set = {i * 15 for i in xrange(100)}

my_dict = {i: i * i for i in range(100)}
my_set = {i * 15 for i in range(100)}

# There is only a difference of ':' in both

# 两者的区别在于字典推导中有冒号

################3.强制浮点除法

result = 1 / 2
# print(result)
# 0.5

################4.对Python表达式求值

# 我们都知道eval函数，但是我们知道literal_eval函数么？也许很多人都不知道吧。可以用这种操作：


expr = "[1, 2, 3]"
my_list = ast.literal_eval(expr)
print(my_list)

# 来代替以下这种操作：

my_list = eval(expr)
print(my_list)

# 我相信对于大多数人来说这种形式是第一次看见，但是实际上这个在Python中已经存在很长时间了。


################5.字符串 / 数列逆序

# 你可以用以下方法快速逆序排列数列：

a = [1, 2, 3, 4]
a[::-1]
# [4, 3, 2, 1]
print(a)
print(a[::-1])

# This creates a new reversed list.
# If you want to reverse a list in place you can do:

a.reverse()
print(a)

# 这总方式也同样适用于字符串的逆序：

foo = "yasoob"
print(foo[::-1])
# 'boosay'


################6.三元运算
# 三元运算是if -else 语句的快捷操作，也被称为条件运算。这里有几个例子可以供你参考，它们可以让你的代码更加紧凑，更加美观。

# [on_true] if [expression] else [on_false]
x, y = 50, 25
small = x if x < y else y

################7.Python里面如何拷贝一个对象
# 标准库中的copy模块提供了两个方法来实现拷贝.一个方法是copy, 它返回和参数包含内容一样的对象.

new_list = copy.copy(existing_list)

# 有些时候, 你希望对象中的属性也被复制, 可以使用deepcopy方法:

new_list_of_dicts = copy.deepcopy(existing_list_of_dicts)
copy(x)
# Shallow copy operation on arbitrary Python objects.

deepcopy(x, memo=None, _nil=[])
# Deep copy operation on arbitrary Python objects.

################8. python中如何判断对象相等
    # 首先是C#中字符串的==和equal方法。
    # “==” :
    # 对于内置值类型而言， == 判断两个内存值是否相等。
    # 对于用户自定义的值类型而言(Struct)， == 需要重载，否则不能使用。
    # 对于引用类型而言，默认是同一引用才返回true，但是系统重载了很多引用类型的 == （比如下文提到的string），所以c#中引用类型的比较并不建议使用 ==。
    # “equals” :
    # 对于值类型而言， 内存相等才返回true。
    # 对于引用类型而言，指向同一个引用才算相等。
    # 但是比较特殊的是字符串String,是一个特殊的引用型类型，在C#语言中，重载了string的equals()方法，使string对象用起来就像是值类型一样。
    # python中的 ==
    # python中的对象包含三要素:id, type, value
    # id 用来标识唯一一个对象，type标识对象的类型，value用来设置对象的值。
    # is 判断是否是一个对象，使用id来判断的。
    # == 是判断a对象的值是否是b对象的值，默认调用它的__eq__方法。

################9. 命名技巧

# 今天阅读代码，发现一个不错的函数命名方式:

def request(_argv):
    print()

# 就是把所有的参数前面都加上_下划线，这样你在函数体中，一眼就可以看出那些是局部变量，那些是作为参数传入的，类似把全局变量前面加上g。


################10.开发者工具集锦

# pydoc： 模块可以根据源代码中的docstrings为任何可导入模块生成格式良好的文档。
# doctest模块：该模块可以从源代码或独立文件的例子中抽取出测试用例。
# unittest模块：该模块是一个全功能的自动化测试框架，该框架提供了对测试准备(test
# fixtures), 预定义测试集(predefined
# test
# suite)以及测试发现(test
# discovery)的支持。
# trace：模块可以监控Python执行程序的方式，同时生成一个报表来显示程序的每一行执行的次数。这些信息可以用来发现未被自动化测试集所覆盖的程序执行路径，也可以用来研究程序调用图，进而发现模块之间的依赖关系。编写并执行测试可以发现绝大多数程序中的问题，Python使得debug工作变得更加简单，这是因为在大部分情况下，Python都能够将未被处理的错误打印到控制台中，我们称这些错误信息为traceback。如果程序不是在文本控制台中运行的，traceback也能够将错误信息输出到日志文件或是消息对话框中。当标准的traceback无法提供足够的信息时，可以使用cgitb
# 模块来查看各级栈和源代码上下文中的详细信息，比如局部变量。cgitb模块还能够将这些跟踪信息以HTML的形式输出，用来报告web应用中的错误。
# pdb：该模块可以显示出程序在错误产生时的执行路径，同时可以动态地调整对象和代码进行调试。
# profile, timeit: 开发者可以使用profile以及timit模块来测试程序的速度，找出程序中到底是哪里很慢，进而对这部分代码独立出来进行调优的工作。
# compileall: Python程序是通过解释器执行的，解释器的输入是原有程序的字节码编译版本。这个字节码编译版本可以在程序执行时动态地生成，也可以在程序打包的时候就生成。compileall模块可以处理程序打包的事宜，它暴露出了打包相关的接口，该接口能够被安装程序和打包工具用来生成包含模块字节码的文件。同时，在开发环境中，compileall模块也可以用来验证源文件是否包含了语法错误。
# YAPF：Google开源的Python代码格式化工具。
# iPDB: iPDB是一个极好的工具，我已经用它查出了很多匪夷所思的bug。pip
# install
# ipdb
# 安装该工具，然后在你的代码中import
# ipdb;
# ipdb.set_trace()，然后你会在你的程序运行时，获得一个很好的交互式提示。它每次执行程序的一行并且检查变量。
# pycallgraph: 在一些场合，我使用pycallgraph来追踪性能问题。它可以创建函数调用时间和次数的图表。
# objgraph: objgraph对于查找内存泄露非常有用。


################11.Python代码微优化之加快查找

collections.OrderedDict类：

def __setitem__(self, key, value, dict_setitem=dict.__setitem__):
    if key not in self:
        root = self.__root
        last = root[0]
        last[1] = root[0] = self.__map[key] = [last, root, key]
    return dict_setitem(self, key, value)


# 注意最后一个参数：dict_setitem = dict.setitem。如果你仔细想就会感觉有道理。将值关联到键上，
# 你只需要给__setitem__传递三个参数：要设置的键，与键关联的值，传递给内建dict类的__setitem__类方法。等会，好吧，也许最后一个参数没什么意义。
# 最后一个参数其实是将一个函数绑定到局部作用域中的一个函数上。具体是通过将dict.__setitem__赋值为参数的默认值。这里还有另一个例子：

def not_list_or_dict(value):
    return not (isinstance(value, dict) or isinstance(value, list))


def not_list_or_dict(value, _isinstance=isinstance, _dict=dict, _list=list):
    return not (_isinstance(value, _dict) or _isinstance(value, _list))


# 这里我们做同样的事情，把本来将会在内建命名空间中的对象绑定到局部作用域中去。因此，python将会使用LOCAL_FAST而不是LOAD_GLOBAL（全局查找）。那么这到底有多快呢？我们做个简单的测试：

# $ python - m timeit - s 'def not_list_or_dict(value): return not (isinstance(value, dict) or isinstance(value, list))' 'not_list_or_dict(50)' 1000000 loops, best of 3: 0.48 usec per loop
# $ python - m timeit - s 'def not_list_or_dict(value, _isinstance=isinstance, _dict=dict, _list=list): return not
#  (_isinstance(value, _dict) or _isinstance(value, _list))' 'not_list_or_dict(50)' 1000000 loops, best of 3: 0.423 usec per loop

# 换句话说，大概有11.9 % 的提升[2]。比我在文章开始处承诺的5 % 还多！

################12. 包管理
# Python世界最棒的地方之一，就是大量的第三方程序包。同样，管理这些包也非常容易。按照惯例，会在 requirements.txt 文件中列出项目所需要的包。每个包占一行，通常还包含版本号。

    # pelican==3.3
    # Markdown
    # pelican-extended-sitemap==1.0.0

################13. Python函数参数默认值的陷阱和原理深究

    # Python 2.7.9 (default, Dec 19 2014, 06:05:48)
    # [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)] on darwin
    # Type "help", "copyright", "credits" or "license" for more information.
def generate_new_list_with(my_list=[], element=None):
    my_list.append(element)
    return my_list

list_1 = generate_new_list_with(element=1)
list_2 = generate_new_list_with(element=2)

# 可见代码运行结果并不和我们预期的一样。list_2在函数的第二次调用时并没有得到一个新的list并填入2，
# 而是在第一次调用结果的基础上append了一个2。为什么会发生这样在其他编程语言中简直就是设计bug一样的问题呢？
# 可见如果参数默认值是在函数编译compile阶段就已经被确定。之后所有的函数调用时，如果参数不显示的给予赋值，那么所谓的参数默认值不过是一个指向那个在compile阶段就已经存在的对象的指针。
# 如果调用函数时，没有显示指定传入参数值得话。那么所有这种情况下的该参数都会作为编译时创建的那个对象的一种别名存在。
# 如果参数的默认值是一个不可变(Imuttable)数值，那么在函数体内如果修改了该参数，那么参数就会重新指向另一个新的不可变值。
# 而如果参数默认值是和本文最开始的举例一样，是一个可变对象(Muttable)，那么情况就比较糟糕了。
# 所有函数体内对于该参数的修改，实际上都是对compile阶段就已经确定的那个对象的修改。


