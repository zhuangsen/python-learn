# -*- coding: utf-8 -*-
# 生成列表
#
# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，我们可以用range(1, 11)：
#
# >>> range(1, 11)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
#
# >>> L = []
# >>> for x in range(1, 11):
# ...    L.append(x * x)
# ...
# >>> L
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
#
# >>> [x * x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# 这种写法就是Python特有的列表生成式。利用列表生成式，可以以非常简洁的代码生成 list。
#
# 写列表生成式时，把要生成的元素 x * x 放到前面，后面跟 for 循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
# 任务
#
# 请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
#
# 提示：range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...]

print [x * (x + 1) for x in range(1, 100, 2)]