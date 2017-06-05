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

    def self_introduction(self):
        print 'My name is %s \n I am %s years old\n' % (self.name, self._age)


class BackendProgramer(Programer):
    def __init__(self, name, age, weight, language):
        super(BackendProgramer, self).__init__(name, age, weight)
        self.language = language

    def self_introduction(self):
        print 'My name is %s \n My favorite language is %s\n' % (self.name, self.language)


def introduction(programer):
    if isinstance(programer, Programer):
        programer.self_introduction()


if __name__ == '__main__':
    programer = Programer('Madison', 25, 60)
    backend_programer = BackendProgramer('Tim', 27, 70, 'Python')
    introduction(programer)
    introduction(backend_programer)
    print Programer.get_hobby()
    print programer.get_weight
