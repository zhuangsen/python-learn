# -*- coding: utf-8 -*-
import io
f = open('F:\\test.txt')

# f = open('f:\\1.txt', 'w')  # 新建文件，里面如果有内容清空
# f = open('f:\\1.txt', 'a')  # 追加方式
# f = open('f:\\1.txt', 'r+')  # 替换文件开头内容
# f = open('f:\\1.txt', 'w+')  # 清空当前文件
# f.write('test')

# readline:读取一行
# print f.readline()
# print f.readline(2)
# print f.readline(2)

# readlines:读取DEFAULT_BUFFER_SIZE左右大小的字节，返回每一行所组成的列表
# print io.DEFAULT_BUFFER_SIZE
# L = f.readlines()
# print L

iter_f = iter(f)
lines = 0
for line in iter_f:
    lines += 1

print(lines)
f.close()
