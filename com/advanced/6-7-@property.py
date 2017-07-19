# -*- coding: utf-8 -*-
# python中 @property
#
# 考察 Student 类：
#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
# 当我们想要修改一个 Student 的 scroe 属性时，可以这么写：
#
# s = Student('Bob', 59)
# s.score = 60
#
# 但是也可以这么写：
#
# s.score = 1000
#
# 显然，直接给属性赋值无法检查分数的有效性。
#
# 如果利用两个方法：
#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#     def get_score(self):
#         return self.__score
#     def set_score(self, score):
#         if score < 0 or score > 100:
#             raise ValueError('invalid score')
#         self.__score = score
#
# 这样一来，s.set_score(1000) 就会报错。
#
# 这种使用 get/set 方法来封装对一个属性的访问在许多面向对象编程的语言中都很常见。
#
# 但是写 s.get_score() 和 s.set_score() 没有直接写 s.score 来得直接。
#
# 有没有两全其美的方法？----有。
#
# 因为Python支持高阶函数，在函数式编程中我们介绍了装饰器函数，可以用装饰器函数把 get/set 方法“装饰”成属性调用：
#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#     @property
#     def score(self):
#         return self.__score
#     @score.setter
#     def score(self, score):
#         if score < 0 or score > 100:
#             raise ValueError('invalid score')
#         self.__score = score
#
# 注意: 第一个score(self)是get方法，用@property装饰，第二个score(self, score)是set方法，用@score.setter装饰，@score.setter是前一个@property装饰后的副产品。
#
# 现在，就可以像使用属性一样设置score了：
#
# >>> s = Student('Bob', 59)
# >>> s.score = 60
# >>> print(s.score
# 60
# >>> s.score = 1000
# Traceback (most recent call last):
#   ...
# ValueError: invalid score
#
# 说明对 score 赋值实际调用的是 set方法。
# 任务
#
# 如果没有定义set方法，就不能对“属性”赋值，这时，就可以创建一个只读“属性”。
#
# 请给Student类加一个grade属性，根据 score 计算 A（>=80）、B、C（<60）。


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.score < 60:
            return 'C'
        if self.score < 80:
            return 'B'
        return 'A'


s = Student('Bob', 59)
print(s.grade)

s.score = 60
print(s.grade)

s.score = 99
print(s.grade)
