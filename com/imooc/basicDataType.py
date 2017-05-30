# -*- coding: utf-8 -*-

# Enter a code
print 45678 + 0x12fd2
print "Learn Python in imooc"
print 100 < 99
print 0xff == 255

# input code
# print语句也可以跟上多个字符串，用逗号“,”隔开，就可以连成一串输出：
print "hello,python"
print "hello,", "python"

x1 = 1
d = 3
n = 100
x100 = d * n - 2
s = (x1 + x100) * n / 2
print s

s = 'Python was started in \'1989\' by "Guido".\nPython is free and easy to learn.'
print s

print r'''"To be,or not to be":that is the question.
Whether it's nobler in the mind to suffer.'''

print '''"To be,or not to be":that is the question.
Whether it's nobler in the mind to suffer.'''

print u'''静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。'''

# Python中整数和浮点数
print 2.5 + 10.0 / 4

# Python中布尔类型

# 因为Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
a = 'python'
print 'hello,', a or 'world'

b = ''
print 'hello,', b or 'world'
