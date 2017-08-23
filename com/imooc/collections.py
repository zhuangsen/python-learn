# -*- coding: utf-8 -*-

# Python创建list
L = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59]
print(L)

# Python按照索引访问list
L = [95.5, 85, 59, 59]
print(L[0])
print(L[1])
print(L[2])
print(L[3])

# Python之倒序访问list
L = [95.5, 85, 59]
print(L[-1])
print(L[-2])
print(L[-3])
# print(L[-4]

# Python之添加新元素
# append()总是把新的元素添加到 list 的尾部。
L = ['Adam', 'Lisa', 'Bart']
L.insert(2, 'Paul')
L.append("Tina")
print(L)

# Python从list删除元素
L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(2)
L.pop(2)
print(L)

# Python中替换元素
L = ['Adam', 'Lisa', 'Bart']
L[2] = 'Adam'
L[0] = 'Bart'
L[-1] = 'Paul'
print(L)

# Python之创建tuple
# tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t)

# Python之创建单元素tuple
# 因为()既可以表示tuple，又可以作为括号表示运算时的优先级，
# 结果 (1) 被Python解释器计算出结果 1，导致我们得到的不是tuple，而是整数 1。
t = ('Adam',)
m = (1)
print(t)
print(m)

# Python之“可变”的tuple
t = ('a', 'b', ['A', 'B'])
l = t[2]
l[0] = 'X'
l[1] = "Y"
print(t)
