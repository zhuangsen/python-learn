# -*- coding: utf-8 -*-
class Programer(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __eq__(self, other):
        if isinstance(other, Programer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of object must be Programer')

    def __add__(self, other):
        if isinstance(other, Programer):
            return self.age + other.age
        else:
            raise Exception('The type of object must be Programer')


if __name__ == '__main__':
    p1 = Programer('Maadison', 25)
    p2 = Programer('Tim', 30)
    print(p1 == p2)
    print(p1 + p2)
