# -*- coding: utf-8 -*-
import os

try:
    with open('1.txt') as f:
        for line in f.read():
            print line
            f.seek(-5, os.SEEK_SET)
except IOError, e:
    print 'in with catch IOError: ', e
    print 'with: ', f.closed

print 'with :', f.closed


class Mycontext(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print '__enter__'
        return self

    def do_self(self):
        print 'do__self'

    def __exit__(self, exc_type, exc_value, traceback):
        print '__exit__'
        print 'Error: ', exc_type, ' info: ', exc_value


if __name__ == '__main__':
    with Mycontext('test context') as f:
        print f.name
        f.do_self()
