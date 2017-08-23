# -*- coding: utf-8 -*-
try:
    a
except NameError as e:
    print('catch Error:', e)
print('exec error')

try:
    undef
except:
    print('catch an except')

# 语法错误，不会执行
# try:
#     if undef
# except:
#     print('catch an except'

try:
    undef
# except NameError, e: # python 2
except NameError as e:
    print(('catch an Name except:', e))

# 捕获不了异常
# try:
#     undef
# except IOError, e:
#     print('catch an IO except:', e

# import random
# num = random.randint(0, 100)
#
# while True:
#     try:
#         guess = int(raw_input('Enter 1~100:'))
#     except ValueError, e:
#         print('Enter 1~100'
#         continue
#     if guess > num:
#         print('guess Bigger:', guess
#     elif guess < num:
#         print('guess Smaller:', guess
#     else:
#         print("Guess OK. Game Over"
#         break
#     print('\n'


try:
    f = open('1.txt')
    line = f.read(4)
    num = int(line)
    print('read num=%d' % num)
except IOError as e:
    print('catch IOError:', e)
except ValueError as e:
    print('catch ValueError:', e)
else:
    print('else clause')
finally:
    try:
        print('finally clause')
        f.close()
    except NameError as e:
        print('catch NameError:', e)

try:
    f = open('1.txt')
    print(int(f.read()))
finally:
    print('close file')
    f.close()
