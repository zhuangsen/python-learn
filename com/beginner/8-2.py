# -*- coding: utf-8 -*-
# 倒序切片
#
# 对于list，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
#
# >>> L = ['Adam', 'Lisa', 'Bart', 'Paul']
#
# >>> L[-2:]
# ['Bart', 'Paul']
#
# >>> L[:-2]
# ['Adam', 'Lisa']
#
# >>> L[-3:-1]
# ['Lisa', 'Bart']
#
# >>> L[-4:-1:2]
# ['Adam', 'Bart']
#
# 记住倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引。
# 任务
#
# 利用倒序切片对 1 - 100 的数列取出：
#
# * 最后10个数；
#
# * 最后10个5的倍数。

L = range(1, 101)
print L[-10:]
print L[-46::5]