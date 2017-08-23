# -*- coding: utf-8 -*-
class Programer(object):
    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight


if __name__ == '__main__':
    programer = Programer('Madison', 25, 60)
    print(dir(programer))
    print(programer.__dict__)
    print(programer.get_weight())
    print(programer._Programer__weight)
