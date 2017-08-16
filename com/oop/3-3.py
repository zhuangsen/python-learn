# -*- coding: utf-8 -*-
class Programer(object):
    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_intruduction(self):
        print('My name is %s \n I am %s years old\n' % (self.name, self._age))


if __name__ == '__main__':
    programer = Programer('Madison', 25, 60)
    print(dir(programer))
    print(programer.get_hobby())
    print(programer.get_weight)
    print(programer.self_intruduction())
