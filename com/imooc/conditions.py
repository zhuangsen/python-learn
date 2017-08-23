# -*- coding: utf-8 -*-
# Python之if语句
# 缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格，否则很容易造成因为缩进引起的语法错误。
score = 75
if score >= 60:
    print('passed')

# Python之 if-else
score = 55
if score >= 60:
    print('passed')
else:
    print('failed')

# Python之 if-elif-else
score = 85
if score >= 90:
    print('excellent')
elif score >= 80:
    print('good')
elif score >= 60:
    print('passed')
else:
    print('failed')

# Python之 for循环
L = [75, 92, 59, 68]
sum = 0.0
for i in L:
    sum += i
print(sum / 4)

# Python之 while循环
sum = 0
x = 1
while x < 100:
    sum += x
    x += 2
print(sum)

# Python之 break退出循环
sum = 0
x = 1
n = 1
while True:
    sum += x
    n = n + 1
    x *= 2
    if n > 20:
        break
print(sum)

# Python之 continue继续循环
sum = 0
x = 0
while True:
    x += 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum += x
print(sum)

# Python之 多重循环
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print(10 * x + y)
