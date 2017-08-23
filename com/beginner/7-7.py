# -*- coding: utf-8 -*-
# Python之定义可变参数
#
# 如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数：
#
# def fn(*args):
#     print(args
#
# 可变参数的名字前面有个 * 号，我们可以传入0个、1个或多个参数给可变参数：
#
# >>> fn()
# ()
# >>> fn('a')
# ('a',)
# >>> fn('a', 'b')
# ('a', 'b')
# >>> fn('a', 'b', 'c')
# ('a', 'b', 'c')
#
# 可变参数也不是很神秘，Python解释器会把传入的一组参数组装成一个tuple传递给可变参数，因此，在函数内部，直接把变量 args 看成一个 tuple 就好了。
#
# 定义可变参数的目的也是为了简化调用。假设我们要计算任意个数的平均值，就可以定义一个可变参数：
#
# def average(*args):
#     ...
#
# 这样，在调用的时候，可以这样写：
#
# >>> average()
# 0
# >>> average(1, 2)
# 1.5
# >>> average(1, 2, 2, 3, 4)
# 2.4
#
# 任务
#
# 请编写接受可变参数的 average() 函数。


def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum += x
    return sum / len(args)


print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4))
