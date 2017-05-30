# -*- coding: utf-8 -*-
# 多层表达式
#
# for循环可以嵌套，因此，在列表生成式中，也可以用多层 for 循环来生成列表。
#
# 对于字符串 'ABC' 和 '123'，可以使用两层循环，生成全排列：
#
# >>> [m + n for m in 'ABC' for n in '123']
# ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
#
# 翻译成循环代码就像下面这样：
#
# L = []
# for m in 'ABC':
#     for n in '123':
#         L.append(m + n)
#
# 任务
#
# 利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。

print [100 * x + 10 * y + z for x in range(1, 10) for y in range(0, 10) for z in range(0, 10) if x == z]
