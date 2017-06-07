# -*- coding: utf-8 -*-
# python把函数作为参数
#
# 在2.1小节中，我们讲了高阶函数的概念，并编写了一个简单的高阶函数：
#
# def add(x, y, f):
#     return f(x) + f(y)
#
# 如果传入abs作为参数f的值：
#
# add(-5, 9, abs)
#
# 根据函数的定义，函数执行的代码实际上是：
#
# abs(-5) + abs(9)
#
# 由于参数 x, y 和 f 都可以任意传入，如果 f 传入其他函数，就可以得到不同的返回值。
# 任务
#
# 利用add(x,y,f)函数，计算：
#

import math


def add(x, y, f):
    return f(x) + f(y)


print add(25, 9, math.sqrt)
