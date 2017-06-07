# -*- coding: utf-8 -*-
# 1.NameError
# a

# 2.SyntaxError
# if a

# 3.IndentationError: expected an indented block
# if a:

# NameError: name 'a' is not defined
# if a:
    # print a

# 4.IOError: [Errno 2] No such file or directory: 'test.txt'
# f = open('test.txt')

# 5.ZeroDivisionError: integer division or modulo by zero
# 10/0

# 6.ValueError: invalid literal for int() with base 10: 'a'
# a = int('a')

# 7.KeyboardInterrupt
import time
for i in range(10):
    time.sleep(2)
