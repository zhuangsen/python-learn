# -*- coding: utf-8 -*-

# print语句可以向屏幕上输出指定的文字。比如输出'hello, world'，用代码实现如下：

# >>> print 'hello, world'

# 注意：

# 1.当我们在Python交互式环境下编写代码时，>>>是Python解释器的提示符，不是代码的一部分。

# 2.当我们在文本编辑器中编写代码时，千万不要自己添加 >>>。

# print语句也可以跟上多个字符串，用逗号“,”隔开，就可以连成一串输出：

# >>> print 'The quick brown fox', 'jumps over', 'the lazy dog'
# The quick brown fox jumps over the lazy dog

# print会依次打印每个字符串，遇到逗号“,”会输出一个空格，因此，输出的字符串是这样拼起来的：

# print也可以打印整数，或者计算结果：

# >>> print 300
# 300    #运行结果
# >>> print 100 + 200
# 300    #运行结果

# 因此，我们可以把计算100 + 200的结果打印得更漂亮一点：

# >>> print '100 + 200 =', 100 + 200
# 100 + 200 = 300     #运行结果

# 注意: 对于100 + 200，Python解释器自动计算出结果300，但是，'100 + 200 ='是字符串而非数学公式，Python把它视为字符串，请自行解释上述打印结果。
# 任务

# 请用两种方式打印出 hello, python.

# input code
# print "hello,python"
# print "hello,", "python"

import math
import random

print("hello world!")
print(math.cos(math.pi))
# 整形
a = 1
# 浮点型
b = 1.2
# 布尔型
c = True
# 字符串
d = "false"
# NoneType
e = None

# 列表
f = [1, 2, 3, 4]
g = list("hello")
# *操作符是对列表的复制，了分段的列表
h = [0] * 3 + [1] * 4
print(f)
print(g)
print(h)
# 列表操作
print(f.pop())
print(f)
f.append(6)
print(f)
print(f.index(6))
# 列表拼接
f += [2, 8, 9]
print(f)
# 下标1处插入0
f.insert(1, 0)
print(f)
# 移除第一个6
f.remove(6)
print(f)
# 赋值下标2
f[2] = 6
print(f)
# 从下标2开始到5之前的子列表
print(f[2:5])

i = list(range(10))
print(i)
# 打乱列表h
random.shuffle(h)
print(h)
